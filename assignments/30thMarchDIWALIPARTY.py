# DIWALI PARTY
# On the festival of Diwali, people decorate their houses with colorful lights. Rahul wants to decorate his house in a unique way. He has a string s representing the pattern of lights he wants to use. Each character in the string represents a lightbulb ('*') or an empty space ('.'). Rahul wants to know the maximum number of consecutive lightbulbs he can use without violating the following rule:

# There should be at least one empty space ('.') between every two already present consecutive lightbulbs, meaning that let's say you were given

# (* ... ') these stars are already present and thus there needs to be atleast one space between them. So the largest sequence comes out to be (*** . *), remember that you have to check the condition add an empty space between the series of already present stars.

# Write a function maxConsecutiveLights to help Rahul determine the maximum number of consecutive lightbulbs he can use in the given string.

# Input:

# A single string s (1 <= |s| <= 10^4), where s contains only '*' and '.' characters.

# Output:

# An integer representing the maximum number of consecutive lightbulbs that can be used in the given string.

# Example:

# Input
# *.*.*
# Output
# 1
# Example

# Input:

# *....*.*.....*
# Output
# 5
# Character 1: *

# currentConsecutive is reset to 0.
# maxConsecutive remains 0.
# Character 2: .

# Increment currentConsecutive to 1.
# Update maxConsecutive to 1.
# Character 3: .

# Increment currentConsecutive to 2.
# Update maxConsecutive to 2.
# Character 4: .

# Increment currentConsecutive to 3.
# Update maxConsecutive to 3.
# Character 5: .

# Increment currentConsecutive to 4.
# Update maxConsecutive to 4.
# Character 6: *

# currentConsecutive is reset to 0.
# maxConsecutive remains 4.
# Character 7: .

# Increment currentConsecutive to 1.
# maxConsecutive remains 4.
# Character 8: *

# currentConsecutive is reset to 0.
# maxConsecutive remains 4.
# Character 9: .

# Increment currentConsecutive to 1.
# maxConsecutive remains 4.
# Character 10: .

# Increment currentConsecutive to 2.
# maxConsecutive remains 4.
# Character 11: .

# Increment currentConsecutive to 3.
# maxConsecutive remains 4.
# Character 12: .

# Increment currentConsecutive to 4.
# maxConsecutive remains 4.
# Character 13: .

# Increment currentConsecutive to 5.
# Update maxConsecutive to 5 (since currentConsecutive > maxConsecutive).
# Character 14: *

# currentConsecutive is reset to 0.
# maxConsecutive remains 5.
# Final Output: At the end of the string, the function finds that the longest sequence of consecutive spaces (.) is 5

# Constraints

# 1 <= |s| <= 10^4

def maxConsecutiveLights(s: str) -> int:
    max_consecutive_spaces = 0
    current_consecutive_spaces = 0
    
    for char in s:
        if char == '.':
            current_consecutive_spaces += 1
            max_consecutive_spaces = max(max_consecutive_spaces, current_consecutive_spaces)
        elif char == '*':
            current_consecutive_spaces = 0
    
    return max_consecutive_spaces

# Test cases
print(maxConsecutiveLights("*.*.*"))         # Output: 1
print(maxConsecutiveLights("*....*.*.....*")) # Output: 5
