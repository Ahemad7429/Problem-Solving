
# String Analysis
# Write a program that counts the number of letters, spaces, numbers, and other characters in a given input string.
# The program takes a string as input and outputs the counts of each category.

# Input Format:
# The input consists of a single string that may contain alphabets, spaces, numbers, and special characters. The length of the string is between 1 and 1000 characters.
# Output Format:
# The program outputs four integers separated by spaces, representing the counts of letters, spaces, numbers, and special characters in the input string, respectively.
# Sample Input:
# Hello World! 123
# Sample Output:
# 10 2 3 1
# Constraints:
# 1 <= Length of input string <= 1000
# Explanation:
# Input string is "Hello World! 123". The program counts 10 letters (including spaces), 2 spaces, 3 numbers, and 1 special character (the exclamation mark), resulting in the output "10 2 3 1".

class Solution:
    def analyze_string(input_string):
        digits = 0
        spaces = 0
        letterCounts = 0
        specialChar = 0
        for i in range(len(input_string)):
            asciiValue = ord(input_string[i])
            if(input_string[i].isdigit()):
                digits += 1
            elif (asciiValue >= 65 and asciiValue <= 90) or (asciiValue >= 97 and asciiValue <= 122):
                letterCounts += 1
            elif input_string[i] == " ":
                spaces += 1
            else:
                specialChar += 1

        print(letterCounts, end= " ")
        print(spaces, end=" ")
        print(digits, end=" ")
        print(specialChar)

            


Solution.analyze_string('Hello World! 123')