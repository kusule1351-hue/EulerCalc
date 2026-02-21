import io
import contextlib
import tkinter as tk

import ttkbootstrap as ttk
from ttkbootstrap.widgets.scrolled import ScrolledText

import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
)

import calculations

TRANSFORMS = standard_transformations + (implicit_multiplication_application,)

TEXT_VARS = {
    "expr", "expression", "eq", "equation", "var", "var1", "var2", "var3",
    "matrix", "A", "B", "f", "g", "bc", "ic", "dir", "mode", "showV", "V"
}


def _extract_equation_token(title: str):
    for tok in (title or "").split():
        if "=" in tok and tok.count("=") == 1:
            return tok
    return None


def _sympy_parse(s: str, locals_: dict):
    s = (s or "").strip().replace("^", "**")
    if s == "":
        raise ValueError("Empty expression")
    return parse_expr(s, local_dict=locals_, transformations=TRANSFORMS)


def _infer_solve_from_title(formula_title: str, var_list: list[str], values: dict):
    tok = _extract_equation_token(formula_title)
    if not tok:
        return None

    left_s, right_s = tok.split("=", 1)
    left_s, right_s = left_s.strip(), right_s.strip()
    if not left_s or not right_s:
        return None

    locals_ = {v: sp.Symbol(v) for v in var_list}
    locals_.update({"pi": sp.pi, "e": sp.E})

    try:
        L = _sympy_parse(left_s, locals_)
        R = _sympy_parse(right_s, locals_)
    except Exception:
        return None

    eq = sp.Eq(L, R)

    unknowns = []
    subs = {}

    for v in var_list:
        val = values.get(v, None)

        if val is None:
            unknowns.append(v)
            continue
        if isinstance(val, sp.Symbol) and str(val) == "x":
            unknowns.append(v)
            continue
        if isinstance(val, str) and val.lower() == "x":
            unknowns.append(v)
            continue

        try:
            subs[locals_[v]] = sp.sympify(val)
        except Exception:
            unknowns.append(v)

    if len(unknowns) != 1:
        return None

    target = locals_[unknowns[0]]
    try:
        sol = sp.solve(eq.subs(subs), target)
    except Exception:
        return None

    if not sol:
        return None
    return sol[0] if len(sol) == 1 else sol


class SimplePhyModern(ttk.Window):
    def __init__(self):
        super().__init__(themename="cyborg")

        self.title("EulerCalc")
        self.geometry("1200x760")
        self.minsize(980, 640)

        if not hasattr(calculations, "CATEGORIES"):
            raise RuntimeError("calculations.py has no CATEGORIES (GUI-ready calculations required).")

        self.all_formulas = self._load_all_formulas()
        self.visible_formulas = list(self.all_formulas)

        self.current = None
        self.input_entries = {}

        self._build_ui()
        self._rebuild_tree()

    def _load_all_formulas(self):
        rows = []
        for cat, getter in calculations.CATEGORIES.items():
            try:
                formulas = getter()
            except Exception:
                formulas = []
            for (name, func, var_list) in formulas:
                rows.append((cat, name, func, var_list))
        return rows

    def _build_ui(self):
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        left = ttk.Frame(self, padding=15)
        left.grid(row=0, column=0, sticky="nsw")
        left.columnconfigure(0, weight=1)
        left.rowconfigure(2, weight=1)

        ttk.Label(left, text="EulerCalc", font=("Segoe UI", 20, "bold")).grid(row=0, column=0, sticky="w")

        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *_: self._apply_search())
        ttk.Entry(left, textvariable=self.search_var, bootstyle="dark").grid(row=1, column=0, pady=10, sticky="ew")

        tree_wrap = ttk.Frame(left)
        tree_wrap.grid(row=2, column=0, sticky="nsew")

        self.tree = ttk.Treeview(tree_wrap, show="tree", bootstyle="dark")
        self.tree.pack(side="left", fill="both", expand=True)

        scroll = ttk.Scrollbar(tree_wrap, orient="vertical", command=self.tree.yview)
        scroll.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scroll.set)

        self.tree.bind("<<TreeviewSelect>>", self._on_tree_select)

        right = ttk.Frame(self, padding=20)
        right.grid(row=0, column=1, sticky="nsew")
        right.columnconfigure(0, weight=1)
        right.rowconfigure(0, weight=1)

        self.tabs = ttk.Notebook(right, bootstyle="dark")
        self.tabs.grid(row=0, column=0, sticky="nsew")

        self.tab_calc = ttk.Frame(self.tabs, padding=10)
        self.tabs.add(self.tab_calc, text="Calculator")
        self.tab_calc.columnconfigure(0, weight=1)
        self.tab_calc.rowconfigure(5, weight=1)

        self.title_lbl = ttk.Label(self.tab_calc, text="Select a formula", font=("Segoe UI", 16, "bold"))
        self.title_lbl.grid(row=0, column=0, sticky="w")

        self.hint_lbl = ttk.Label(
            self.tab_calc,
            text="Unknown: type x (or leave blank). Supports: 1/3, pi, sqrt(2), 1e-3, sin(pi/2).",
            bootstyle="secondary",
            wraplength=820,
        )
        self.hint_lbl.grid(row=1, column=0, sticky="w", pady=(6, 10))

        self.inputs_container = ttk.Frame(self.tab_calc)
        self.inputs_container.grid(row=2, column=0, sticky="ew")
        self.inputs_container.columnconfigure(1, weight=1)

        btn_row = ttk.Frame(self.tab_calc)
        btn_row.grid(row=3, column=0, sticky="w", pady=(12, 0))
        ttk.Button(btn_row, text="Run", bootstyle="success", command=self._run).grid(row=0, column=0, padx=(0, 10))
        ttk.Button(btn_row, text="Clear", bootstyle="secondary", command=self._clear).grid(row=0, column=1)

        ttk.Label(self.tab_calc, text="Result", font=("Segoe UI", 12, "bold")).grid(row=4, column=0, sticky="w", pady=(16, 6))

        self.result = ScrolledText(self.tab_calc, autohide=True, height=16)
        try:
            self.result.text.configure(
                bg="#0b0d12", fg="#e8eaf0", insertbackground="#e8eaf0",
                relief="flat", bd=0, font=("Cascadia Mono", 10),
            )
        except Exception:
            pass
        self.result.grid(row=5, column=0, sticky="nsew")

    def _rebuild_tree(self):
        self.tree.delete(*self.tree.get_children())
        cat_nodes = {}

        for cat, name, _func, _vars in self.visible_formulas:
            if cat not in cat_nodes:
                cat_nodes[cat] = self.tree.insert("", "end", text=cat, open=False)

            base = f"{cat}::{name}"
            iid = base
            k = 2
            while self.tree.exists(iid):
                iid = f"{base} #{k}"
                k += 1

            self.tree.insert(cat_nodes[cat], "end", iid=iid, text=name)

    def _apply_search(self):
        q = (self.search_var.get() or "").strip().lower()
        if not q:
            self.visible_formulas = list(self.all_formulas)
        else:
            self.visible_formulas = [r for r in self.all_formulas if q in r[0].lower() or q in r[1].lower()]
        self._rebuild_tree()

    def _on_tree_select(self, _evt=None):
        sel = self.tree.selection()
        if not sel:
            return

        iid = sel[0]
        if "::" not in iid:
            self.current = None
            self.title_lbl.config(text=self.tree.item(iid, "text"))
            self._render_inputs([])
            return

        cat, name = iid.split("::", 1)
        name = name.split(" #", 1)[0]

        found = None
        for row in self.all_formulas:
            if row[0] == cat and row[1] == name:
                found = row
                break
        if not found:
            return

        self.current = found
        _cat, title, _func, var_list = found
        self.title_lbl.config(text=title)
        self._render_inputs(var_list)

    def _render_inputs(self, var_list):
        for w in self.inputs_container.winfo_children():
            w.destroy()
        self.input_entries.clear()

        for r, v in enumerate(var_list):
            ttk.Label(self.inputs_container, text=v).grid(row=r, column=0, sticky="w", pady=6)
            ent = ttk.Entry(self.inputs_container, bootstyle="dark")
            ent.grid(row=r, column=1, sticky="ew", padx=10, pady=6)
            self.input_entries[v] = ent

    def _parse_user_input(self, raw: str):
        s = (raw or "").strip()
        if s == "":
            return None
        if s.lower() == "x":
            return sp.Symbol("x")

        s = s.replace("^", "**")
        locals_ = {
            "pi": sp.pi, "e": sp.E, "oo": sp.oo, "inf": sp.oo,
            "sin": sp.sin, "cos": sp.cos, "tan": sp.tan,
            "sqrt": sp.sqrt, "log": sp.log, "ln": sp.log, "exp": sp.exp,
        }
        expr = parse_expr(s, local_dict=locals_, transformations=TRANSFORMS)
        return float(expr) if len(getattr(expr, "free_symbols", set())) == 0 else expr

    def _set_result(self, text: str):
        self.result.delete("1.0", "end")
        self.result.insert("end", text)

    def _run(self):
        if not self.current:
            return

        _cat, title, func, var_list = self.current

        values = {}
        for v in var_list:
            raw = (self.input_entries.get(v).get() or "").strip()

            if v in TEXT_VARS:
                values[v] = raw
                continue

            try:
                values[v] = self._parse_user_input(raw)
            except Exception as e:
                self._set_result(f"Input error for '{v}': {e}")
                return

        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                out = func(values)
        except Exception as e:
            out = f"Error: {e}"

        printed = buf.getvalue().strip()

        if out is None and not printed:
            inferred = _infer_solve_from_title(title, var_list, values)
            if inferred is not None:
                out = inferred

        if out is None:
            out = printed if printed else "(No output returned.)"
        else:
            if printed:
                out = str(out) + "\n\n[print output]\n" + printed

        self._set_result(str(out))

    def _clear(self):
        for ent in self.input_entries.values():
            ent.delete(0, "end")
        self._set_result("")


if __name__ == "__main__":
    app = SimplePhyModern()
    app.mainloop()
