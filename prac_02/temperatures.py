"""
Pseudocode:

display MENU  
get choice from user and convert to uppercase  
while choice is not "Q"  
    if choice is "C"  
        get celsius value from user  
        calculate fahrenheit by calling convert_celsius_to_fahrenheit with celsius  
        display result formatted to two decimal places followed by " F"  
    else if choice is "F"  
        get fahrenheit value from user  
        calculate celsius by calling convert_fahrenheit_to_celsius with fahrenheit  
        display result formatted to two decimal places followed by " C"  
    else  
        display "Invalid option"  
    end if  
    display MENU  
    get choice from user and convert to uppercase  
end while  
display "Thank you."  
"""

# Constants
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    """
    Display the menu, handle user choices, and call the appropriate conversion functions.
    """
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")


def convert_celsius_to_fahrenheit(celsius):
    """
    Convert a Celsius temperature to Fahrenheit.
    """
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """
    Convert a Fahrenheit temperature to Celsius.
    """
    return 5.0 / 9 * (fahrenheit - 32)


if __name__ == "__main__":
    main()

