import math
import re
from fractions import Fraction

# Variables treated as plain text (not numeric) in UI/CLI
TEXT_VARS = {
    "expr", "eq", "var", "var1", "var2", "var3",
    "matrix", "A", "B", "dir", "f", "f0", "bc", "g0", "V", "showV"
}

SAFE_FUNCS = {
    "pi": math.pi,
    "e": math.e,
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log10,
    "ln": math.log,
    "exp": math.exp,
    "abs": abs,
}

SAFE_NUM_EVAL = {"__builtins__": None, **SAFE_FUNCS}

def fix_expression(text: str) -> str:
    text = (text or "").strip()
    text = text.replace("^", "**")
    text = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", text)   # 2x -> 2*x
    text = re.sub(r"(\))([a-zA-Z])", r"\1*\2", text)   # )x -> )*x
    text = re.sub(r"([xyz])(\()", r"\1*\2", text)      # x( -> x*(
    text = re.sub(r"(\))(\()", r"\1*\2", text)        # ) ( -> )*(
    return text

def parse_value(text: str):
    """Parse numeric input for known values.
    - '' -> None
    - 'x' -> special marker (string 'x') for unknown (some formulas use this)
    - supports 1/3, pi, sqrt(2), etc.
    """
    s = fix_expression(text)
    if s == "":
        return None
    if s.lower() == "x":
        return "x"

    try:
        return float(Fraction(s))
    except Exception:
        pass

    try:
        return float(eval(s, SAFE_NUM_EVAL, {}))
    except Exception as e:
        raise ValueError(f"Invalid number: {text}") from e

def solve_formula_menu(title, formulas):
    """CLI menu (used by main.py). Keeps behavior simple and robust."""
    while True:
        print(f"\n--- {title} ---")
        for i, (name, _func, _vars) in enumerate(formulas, start=1):
            print(f"{i}. {name}")
        print("0. Back")

        choice = input("Select: ").strip()
        if choice in {"0", "q", "Q", "back", "Back"}:
            return
        if not choice.isdigit():
            print("❌ Please enter a number.")
            continue

        idx = int(choice)
        if idx < 1 or idx > len(formulas):
            print("❌ Invalid choice.")
            continue

        name, func, var_list = formulas[idx - 1]
        print(f"\n--- {name} ---")
        print("Known numbers: 2, 0.5, 1/3, pi, sqrt(2)")
        print("Unknown: type x (or leave empty)")

        values = {}
        for v in var_list:
            user_in = input(f"{v} = ")
            if v in TEXT_VARS:
                values[v] = (user_in or "").strip()
                continue
            try:
                values[v] = parse_value(user_in)
            except Exception as e:
                print(f"❌ {e}")
                values[v] = None

        try:
            result = func(values)
            print("\n✅ Result:\n")
            print(result if result is not None else "(no output)")
        except Exception as e:
            print(f"\n❌ Error: {e}")
