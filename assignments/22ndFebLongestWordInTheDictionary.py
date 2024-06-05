# Longest Word in the Dictionary
# Write a program that takes a dictionary of words as input and finds all the longest words in the dictionary. If there are multiple longest words of the same length, the program should output all of them.

# Input Format:
# The input consists of a list of words in the dictionary. Each word is on a separate line.

# Output Format:
# The program outputs all the longest words found in the dictionary. If there are multiple longest words, they are printed on separate lines.

# Example:
# Input:
# apple
# banana
# orange
# mango
# pineapple
# Output:
# pineapple
# Constraints:
# The length of each word in the dictionary is at most 100 characters.
# The dictionary can contain up to 10^4 words.
# Explanation:
# In the given dictionary, "pineapple" is the longest word with a length of 9 characters. Therefore, the program outputs "pineapple" as the longest word.


class Solution:
    @staticmethod
    def findLongestWords(input_lines):
        max_length = 0
        longest_words = []

        # Find the maximum length of words in the dictionary
        for word in input_lines:
            max_length = max(max_length, len(word))

        # Find all the words with the maximum length
        for word in input_lines:
            if len(word) == max_length:
                longest_words.append(word)

        return longest_words

# Test the function
input_lines = ["apple", "banana", "orange", "mango", "pineapple"]
print(Solution.findLongestWords(input_lines))
