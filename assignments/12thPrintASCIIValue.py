# Print ASCII Value
# Write a program that prints the ASCII value of a given character. The program takes a single character as input and outputs its corresponding ASCII value.

# Input Format:
# The input consists of a single character, which can be any valid ASCII character.

# Output Format:
# The program outputs an integer representing the ASCII value of the input character.

# Sample Input:
# A
# Sample Output:
# 65
# Constraints:
# The input character is a valid ASCII character.
# Explanation:
# Input is the character 'A'. The ASCII value of 'A' is 65, which is printed as the output of the program.

class Solution:
    def print_ascii_value(character):
      print(ord(character))
