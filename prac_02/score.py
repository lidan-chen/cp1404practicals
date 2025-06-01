"""
Pseudocode:

prompt for score
get score as number
if score < 0 or score > 100
    status = "Invalid score"
else if score >= 90
    status = "Excellent"
else if score >= 50
    status = "Passable"
else
    status = "Bad"
end if
print status

generate random_score as integer between 0 and 100
random_status = determine_score_status(random_score)
print "Random score: ", random_score, "→", random_status
"""

import random

def main():
    """
    Prompt for a score, determine its status, and display the result.
    Then generate a random score, determine its status, and display that result.
    """
    # ask user for their score and evaluate
    score = float(input("Enter score: "))
    status = determine_score_status(score)
    print(status)

    # generate and evaluate a random score
    random_score = random.randint(0, 100)
    random_status = determine_score_status(random_score)
    print(f"Random score: {random_score} → {random_status}")


def determine_score_status(score):
    """
    Determine the status string for the given score.
    Return "Invalid score" if outside 0–100;
    "Excellent" if 90 or above;
    "Passable" if 50–89;
    otherwise "Bad".
    """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == "__main__":
    main()

