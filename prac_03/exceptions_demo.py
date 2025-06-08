"""
algorithm:
prompt for valid integer numerator
prompt for valid non-zero integer denominator
calculate numerator divided by denominator
display the result
"""

def main():
    """Prompt for numerator and denominator, validate inputs, perform division and display result."""
    # 1. A ValueError occurs when the user enters something that cannot be converted to an integer (e.g., "abc").
    # 2. A ZeroDivisionError would occur if we tried to divide by zero (denominator == 0).
    # 3. We avoid ZeroDivisionError by validating that the denominator is not zero before dividing.

    while True:
        try:
            numerator = int(input("Enter the numerator: "))
            break
        except ValueError:
            print("Numerator must be a valid integer!")

    while True:
        try:
            denominator = int(input("Enter the denominator: "))
            if denominator == 0:
                print("Denominator cannot be zero! Please enter a non-zero integer.")
                continue
            break
        except ValueError:
            print("Denominator must be a valid integer!")

    fraction = numerator / denominator
    print(fraction)
    print("Finished.")

if __name__ == "__main__":
    main()
