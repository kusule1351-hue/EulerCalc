# main.py

import calculations

def main():
    while True:
        print("\n" + "="*50)
        print("SIMPLE PHY CALCULATOR")
        print("="*50)

        print("1. Mechanics")
        print("2. Thermodynamics + Waves")
        print("3. Gravitation")
        print("4. Fluids")
        print("5. Sound")
        print("6. Electromagnetic")
        print("7. Communication")
        print("8. Semiconductor")
        print("9. Error & Measurement")
        print("10. Magnetism")
        print("11. Optics")
        print("12. Modern Physics")
        print("13. Oscillation")
        print("14. Electric")
        print("15. Math tools(Integral, Derrative, Matrix)")
        print("0. Back")

        ch = input("Choose: ").strip()

        if ch == "1":
            calculations.mechanics_menu()
        elif ch == "2":
            calculations.thermo_menu()
        elif ch == "3":
            calculations.gravitation_menu()
        elif ch == "4":
            calculations.fluids_menu()
        elif ch == "5":
            calculations.sound_menu()
        elif ch == "6":
            calculations.electromagnetic_menu()
        elif ch == "7":
            calculations.communication_menu()
        elif ch == "8":
            calculations.semiconductor_menu()
        elif ch == "9":
            calculations.error_menu()
        elif ch == "10":
            calculations.magnetism_menu()
        elif ch == "11":
            calculations.optics_menu()
        elif ch == "12":
            calculations.modern_menu()
        elif ch == "13":
            calculations.oscillation_menu()
        elif ch == "14":
            calculations.electric_menu()
        elif ch == "15":
            calculations.math_menu()
        elif ch == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice")




if __name__ == "__main__":
    main()
