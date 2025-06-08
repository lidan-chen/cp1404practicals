"""
algorithm:
load random module
generate integer between 5 and 20 inclusive and display it
generate integer from 3 to 9 inclusive in steps of 2 and display it
generate real number between 2.5 and 5.5 and display it
generate integer between 1 and 100 inclusive and display it
"""

import random

def main():
    """Generate and display random numbers and answer questions about their ranges."""
    # line 1: random.randint(5, 20)
    value1 = random.randint(5, 20)
    print(value1)
    # what did you see on line 1?
    # I saw an integer between 5 and 20, for example 13.
    # smallest number: 5
    # largest number: 20

    # line 2: random.randrange(3, 10, 2)
    value2 = random.randrange(3, 10, 2)
    print(value2)
    # what did you see on line 2?
    # I saw an integer from the sequence 3, 5, 7, 9, for example 7.
    # smallest number: 3
    # largest number: 9
    # could line 2 have produced a 4?
    # no, because the sequence only includes numbers starting at 3 in steps of 2.

    # line 3: random.uniform(2.5, 5.5)
    value3 = random.uniform(2.5, 5.5)
    print(value3)
    # what did you see on line 3?
    # I saw a floating point number between 2.5 and 5.5, for example 4.237148.
    # smallest number: 2.5
    # largest number: 5.5

    # generate a random number between 1 and 100 inclusive
    number_1_to_100 = random.randint(1, 100)
    print(number_1_to_100)

if __name__ == "__main__":
    main()
