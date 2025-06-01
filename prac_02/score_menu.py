"""
pseudocode:
set score by getting a valid score from user
display menu options
loop until user chooses "Q"
    get choice from user and convert to uppercase
    if choice is "G"
        set score by getting a valid score from user
    else if choice is "P"
        determine status by calling determine_score_status with score
        print status
    else if choice is "S"
        print stars equal in number to score
    else if choice is "Q"
        exit loop
    else
        print "Invalid option"
    end if
    display menu options again
end loop
print "Goodbye"
"""

def main():
    """
    Display the main menu, handle user selections, and call appropriate functions.
    """
    # get an initial valid score before entering menu loop
    score = get_valid_score()

    while True:
        print_menu()
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_score_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Goodbye")
            break
        else:
            print("Invalid option")


def print_menu():
    """
    Display the menu options to the user.
    """
    print("Menu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """
    Prompt the user until a valid integer score between 0 and 100 inclusive is entered.
    Return the valid score as an integer.
    """
    while True:
        try:
            user_input = input("Enter score (0-100): ")
            value = int(user_input)
            if 0 <= value <= 100:
                return value
            else:
                print("Score must be between 0 and 100")
        except ValueError:
            print("Invalid input; please enter an integer")


def determine_score_status(score):
    """
    Determine the status string for the given score.
    Return "Excellent" if 90 or above;
    "Passable" if 50–89;
    otherwise "Bad".
    """
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_score_result(score):
    """
    Determine the status of the given score and print it.
    """
    status = determine_score_status(score)
    print(status)


def show_stars(score):
    """
    Print a line of stars equal to the given score.
    """
    print("*" * score)


if __name__ == "__main__":
    main()

