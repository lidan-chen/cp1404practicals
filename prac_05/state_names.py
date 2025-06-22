"""
get short state from user
convert short state to uppercase
repeat until input is empty
    try to get state name from dictionary
        print short state and full name
    if error, print invalid short state
    ask for another short state

print all short states and names aligned
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}


def main():
    """Prompt user for state abbreviations and show full state name."""
    state_code = input("Enter short state: ").upper()
    while state_code != "":
        try:
            print(f"{state_code} is {CODE_TO_NAME[state_code]}")
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()

    print("\nAll states:")
    for code, name in CODE_TO_NAME.items():
        print(f"{code:>3} is {name}")


main()
