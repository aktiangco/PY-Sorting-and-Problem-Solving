# Write your solution for algorithm 4 below

def sort_words(string):
    words = string.split()  # Split the string into a list of words
    sorted_words = sorted(words, key=lambda word: word.lower())  # Sort the words case-insensitively
    return sorted_words  # Return the sorted list of words

# Example usage
input_string = 'I love software engineering'
sorted_words = sort_words(input_string)
print(sorted_words)
