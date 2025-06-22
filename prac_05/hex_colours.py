"""
get colour name from user
convert name to title case
repeat until input is blank
    try to get hex code from dictionary
        print colour name and code
    if error, print invalid colour name
    ask for another colour name
"""

COLOUR_HEX_CODES = {
    "Absolute Zero": "#0048ba",
    "Acid Green": "#b0bf1a",
    "AliceBlue": "#f0f8ff",
    "Alizarin crimson": "#e32636",
    "Amaranth": "#e52b50",
    "Amber": "#ffbf00",
    "Amethyst": "#9966cc",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Azure": "#f0ffff"
}


def main():
    """Prompt user for color names and display the hex code if found."""
    color_name = input("Enter color name: ").title()
    while color_name != "":
        try:
            print(f"{color_name} has hex code {COLOUR_HEX_CODES[color_name]}")
        except KeyError:
            print("Invalid color name")
        color_name = input("Enter color name: ").title()


main()
