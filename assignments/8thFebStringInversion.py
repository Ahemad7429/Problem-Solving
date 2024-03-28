# String Inversion
# Write a program that reverses a given string. The program takes a string as input and outputs the reversed string.

# Input Format:
# The input consists of a single string, which may contain alphabets, numbers, and special characters. The length of the string is between 1 and 1000 characters.
# Output Format:
# The program outputs a string representing the reversed version of the input string.
# Sample Input:
# Hello World!
# Sample Output:
# !dlroW olleH
# Constraints:
# 1 <= Length of input string <= 1000


class Solution:
    def reverseString(s):
        ans = ''
        n = len(s)
        i = n - 1
        while i >= 0:
            ans += s[i]
            i -= 1
        return ans
    
print(Solution.reverseString("Hello World!"))