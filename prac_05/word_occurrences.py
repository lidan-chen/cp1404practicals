"""
Word Occurrences
Estimate: 20 minutes
Actual: 18 minutes
"""

"""
get input text from user
split text into words
create empty dictionary
for each word in list of words
    if word in dictionary
        increment count
    else
        add word with count 1
find max length of words for formatting
for each word in dictionary sorted by word
    print word aligned with count
"""

def main():
    """Count and display word occurrences in input text, sorted and aligned."""
    text = input("Text: ")
    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    max_word_length = max(len(word) for word in word_count)

    for word in sorted(word_count):
        print(f"{word:{max_word_length}} : {word_count[word]}")


main()
