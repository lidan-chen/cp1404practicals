"""
Emails
Estimate: 25 minutes
Actual: 21 minutes
"""

"""
ask user for email
repeat until email is blank
    extract name from email using split and title
    ask if the name is correct (default Y)
        if not correct, ask for actual name
    store email and name in dictionary
print all names and emails in format: Name (email)
"""

def main():
    """Store emails and names, prompting user for confirmation or edits."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ("", "y"):
            name = input("Name: ").strip().title()
        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from email by splitting and title-casing parts."""
    name_part = email.split('@')[0]
    name_parts = name_part.replace('.', ' ').replace('_', ' ').split()
    return ' '.join(name_parts).title()


main()
