# Basic Calculator
# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

# Note:
# You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example 1:

# Input: s = "1 + 1"

# Output: 
# 2


# Example 2:

# Input: s = " 2-1 + 2 "
# Output:
#  3
# Example 3:

# Input:
# s = "(1+(4+5+2)-3)+(6+8)"</br> 
# Output:
#   23
# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of digits, '+', '-', '(', ')', and ' '. s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.

def calculate(s: str) -> int:
    def update_stack(op, num):
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)

    stack = []
    num = 0
    op = '+'  # Assume the first number is positive
    i = 0

    while i < len(s):
        char = s[i]

        if char.isdigit():
            num = num * 10 + int(char)
        if char in "+-":
            update_stack(op, num)
            num = 0
            op = char
        if char == '(':
            stack.append(op)
            stack.append('(')
            op = '+'  # Reset default operator for new sub-expression
        if char == ')':
            update_stack(op, num)
            num = 0
            # Evaluate the sub-expression within parentheses
            temp = 0
            while stack and stack[-1] != '(':
                temp += stack.pop()
            stack.pop()  # Remove the '('
            op = stack.pop() if stack else '+'
            num = temp

        i += 1

    update_stack(op, num)  # Add the last number

    return sum(stack)

# Example usage:
print(calculate("1 + 1"))          # Output: 2
print(calculate(" 2-1 + 2 "))      # Output: 3
print(calculate("(1+(4+5+2)-3)+(6+8)"))  # Output: 23

# Sort the Array
# You have to sort the string s in decreasing order based on the frequency of the characters. Return the sorted string. if frequency of two character are same then sort in alphabetical order.

# Example 1
# Input
# s = "tree"
# Output
# "eert"
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once. So 'e' must appear before both 'r' and 't'. "eetr" is not a valid answer as r appears before t.

# Example 2
# Input
#  s = "cccaaa"
# Output
# "aaaccc"
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is valid answer. Note that "cccaaa" is not a valid answer as both 'c' and 'a' appear three times but a comes before c in dictionary. Note that "cacaca" is incorrect, as the same characters must be together.

# Example 3
# Input
#  s = "aA"
# Output
# "Aa"
# Constraints:
# 1 <= s.length <= 5 * 10^5
# s consists of uppercase and lowercase English letters and digits.

def sort_by_frequency(s: str) -> str:
    # Step 1: Count the frequency of each character using a dictionary
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Step 2: Create a list of (character, frequency) tuples
    freq_list = list(freq.items())

    # Step 3: Sort the list based on frequency (descending) and character (alphabetical)
    sorted_chars = sorted(freq_list, key=lambda x: (-x[1], x[0]))

    # Step 4: Build the result string by repeating characters based on their frequency
    result = ''.join(char * count for char, count in sorted_chars)

    return result

# Example usage:
print(sort_by_frequency("tree"))    # Output: "eert"
print(sort_by_frequency("cccaaa"))  # Output: "aaaccc"
print(sort_by_frequency("aA"))      # Output: "Aa"

# Group Anangrams
# Given an array of strings strs, group the anagrams together. You can print the answer in sorted order. Also, output the list of anagrams in sorted order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Input Format:
# first line contains a single integer n (size of the array).
# second line contains n strings.
# Output Format:
# Print the group of anagrams with a single space between them

# Each group in new line
# Constraints:
# 1 <= n <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# Example:
# Input:
# 6
# eat tea tan ate nat bat

# Output:
# ate eat tea
# bat
# nat tan

# Explanation:
# As ate comes before bat so the group of anagrams of ate should come before group of anagrams of bat. same for others.

def group_anagrams(n, strs):
    # Dictionary to store grouped anagrams
    anagrams = {}

    # Grouping the anagrams
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    # Collecting results
    result = []
    for group in sorted(anagrams.values(), key=lambda x: sorted(x)[0]):
        result.append(' '.join(sorted(group)))

    # Printing results
    for line in result:
        print(line)

# Example usage:
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    strs = data[1:n+1]
    group_anagrams(n, strs)
