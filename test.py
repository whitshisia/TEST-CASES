def alphCount(oStr):
    # Filter out non-alphanumeric characters and spaces
    CleanedString = ''.join(filter(lambda x: x.isalpha() or x.isspace() or x.isdigit(), oStr))

    # Convert the string to lowercase
    CleanedString = CleanedString.lower()

    # Create a dictionary with counts of each character
    char_count = {x: CleanedString.count(x) for x in CleanedString if x != ' '}

    # Find the most and least repeated letters
    most_repeated = max(char_count, key=char_count.get)
    least_repeated = min(char_count, key=char_count.get)

    print(f"Most repeated letter: '{most_repeated}' with count {char_count[most_repeated]}")
    print(f"Least repeated letter: '{least_repeated}' with count {char_count[least_repeated]}")

# Example usage
alphCount("My name is shisia.")
