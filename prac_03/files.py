"""
algorithm:
ask user for their name
open 'name.txt' for writing and write the name, then close file
open 'name.txt' for reading and read entire contents, then close file
print greeting using the read name
open 'numbers.txt' for reading with 'with' and read first two lines using readline()
convert those two lines to integers, sum them, and print the result
open 'numbers.txt' for reading with 'with' and iterate over each line (for line in file)
convert each line to integer, accumulate into total, and print the total
"""

def main():
    """Demonstrate various file read/write techniques."""
    # 1. Write user name to 'name.txt'
    name = input("Enter your name: ")
    out_file = open('name.txt', 'w')
    out_file.write(name)
    out_file.close()

    # 2. Read name back from 'name.txt' using read()
    in_file = open('name.txt', 'r')
    stored_name = in_file.read()
    in_file.close()
    print(f"Hi {stored_name}!")

    # 3. Read only the first two numbers from 'numbers.txt' using readline()
    with open('numbers.txt', 'r') as num_file:
        first = num_file.readline()
        second = num_file.readline()
    total_two = int(first) + int(second)
    print(total_two)

    # 4. Sum all numbers in 'numbers.txt' using for line in file
    total_all = 0
    with open('numbers.txt', 'r') as num_file:
        for line in num_file:
            total_all += int(line)
    print(total_all)


if __name__ == "__main__":
    main()
