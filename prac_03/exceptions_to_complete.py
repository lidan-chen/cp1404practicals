"""
algorithm:
set is_finished to false
while is_finished is false:
    prompt for integer input and try to convert to int
    if conversion succeeds:
        set is_finished to true
    otherwise:
        display an error message
display the valid result
"""

def main():
    """Prompt repeatedly until a valid integer is entered, then display it."""
    is_finished = False
    while not is_finished:
        try:
            result = int(input("Enter a valid integer: "))
            is_finished = True
        except ValueError:
            print("Please enter a valid integer.")
    print("Valid result is:", result)

if __name__ == "__main__":
    main()
