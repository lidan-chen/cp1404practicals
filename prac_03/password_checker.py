"""
algorithm:
print password requirements using MIN_LENGTH, MAX_LENGTH, and SPECIAL_CHARACTERS if required
prompt user for a password
while password is not valid:
    print invalid password message
    prompt user again
print confirmation message with password length and the valid password
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Ask for and validate a user's password according to defined rules."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print(f"\tand 1 or more special characters: {SPECIAL_CHARACTERS}")
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Validate password length and character composition."""
    # check length requirements
    if not (MIN_LENGTH <= len(password) <= MAX_LENGTH):
        return False

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0
    for character in password:
        if character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character.isdigit():
            number_of_digit += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1

    # ensure at least one of each required category
    if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0:
        return False

    # ensure special character if required
    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == 0:
        return False

    # password meets all criteria
    return True


if __name__ == "__main__":
    main()
