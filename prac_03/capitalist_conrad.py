"""
algorithm:
load random module
set constants for max increase, max decrease, min price, max price, initial price, and filename
initialize price to initial price
initialize day_count to 0
open output file for writing
write starting price to file
while price is between min price and max price:
    increment day_count
    randomly choose increase or decrease with equal chance
    if increase:
        pick a random change between zero and max increase
    else:
        pick a random change between negative max decrease and zero
    update price by multiplying by (1 + change)
    write "On day {day_count} price is: ${price}" to file
close output file
"""

import random

# constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.0       # $1 minimum
MAX_PRICE = 100.0     # $100 maximum
INITIAL_PRICE = 10.0  # starting price
FILENAME = "prices.txt"  # output filename

def main():
    """Simulate daily stock price changes and write results to a file."""
    price = INITIAL_PRICE
    day_count = 0
    out_file = open(FILENAME, 'w')

    print(f"Starting price: ${price:,.2f}", file=out_file)

    while MIN_PRICE <= price <= MAX_PRICE:
        day_count += 1
        # choose increase or decrease
        if random.randint(1, 2) == 1:
            change = random.uniform(0, MAX_INCREASE)
        else:
            change = random.uniform(-MAX_DECREASE, 0)
        price *= (1 + change)
        print(f"On day {day_count} price is: ${price:,.2f}", file=out_file)

    out_file.close()


if __name__ == "__main__":
    main()
