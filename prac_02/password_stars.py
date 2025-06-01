"""
pseudocode:
call main
    call get_password to prompt user for a password and return it
    if returned password equals correct value
        print "Access granted"
        call print_stars with the password to print asterisks
    else
        print "Access denied"
end main

define get_password
    prompt user for a password string
    if input equals correct value
        return the password
    else
        return none
end get_password

define print_stars with parameter password
    repeat printing "*" for each character in password
end print_stars
"""

def main():
    """
    Prompt for a password, check it, and print asterisks if access is granted.
    """
    password = get_password()
    if password == "letmein":
        print("Access granted")
        print_stars(password)
    else:
        print("Access denied")


def get_password():
    """
    Prompt the user for a password.
    If it matches "letmein", return it; otherwise return None.
    """
    pwd = input("Enter password: ")
    if pwd == "letmein":
        return pwd
    else:
        return None


def print_stars(password, symbol="*"):
    """
    Print one symbol character per character in the provided password.
    By default, prints "*". Can override symbol if desired.
    """
    print(symbol * len(password))


if __name__ == "__main__":
    main()
