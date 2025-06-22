"""
Wimbledon
Estimate: 25 minutes
Actual: 22 minutes
"""

"""
read wimbledon.csv file using utf-8-sig encoding
skip the header line
for each line:
    extract champion name and country
    count champion wins using a dictionary
    add country to a set
print champion names and win counts
print sorted country names using join
"""

FILENAME = "wimbledon.csv"


def main():
    """Read Wimbledon data and display champions and countries."""
    records = read_wimbledon_data(FILENAME)
    champions_to_wins = count_champion_wins(records)
    winning_countries = extract_winning_countries(records)

    print("Wimbledon Champions:")
    for champion, wins in champions_to_wins.items():
        print(f"{champion} {wins}")

    print(f"\nThese {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(sorted(winning_countries)))


def read_wimbledon_data(filename):
    """Read data from CSV file and return list of [champion, country]."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # skip header
        for line in in_file:
            parts = line.strip().split(",")
            country = parts[1]
            champion = parts[2]
            records.append([champion, country])
    return records


def count_champion_wins(data):
    """Return a dictionary of champion names and how many times they won."""
    champion_to_wins = {}
    for champion, _ in data:
        if champion in champion_to_wins:
            champion_to_wins[champion] += 1
        else:
            champion_to_wins[champion] = 1
    return champion_to_wins


def extract_winning_countries(data):
    """Return a set of unique winning countries from the records."""
    return {country for _, country in data}


main()
