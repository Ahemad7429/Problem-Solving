# Lucky Number
# In this challenge, you're tasked with determining whether a given number is a "Lucky Number." A Lucky Number is defined by the following process:

# Start with any positive integer.
# Replace the number with the sum of the cubes of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.
# If, at any stage of this process, the number reaches 1, it is deemed a Lucky Number. Your goal is to create a function that accepts an integer as input and returns true if it is a Lucky Number by reaching 1, and false otherwise.
# For example:
# A number like 100 is a Lucky Number because the process (1^3 + 0^3 + 0^3 = 1) immediately reaches 1. A number like 4 is not a Lucky Number because it enters a cycle (4^3 = 64, 6^3 + 4^3 = 280, 2^3 + 8^3 + 0^3 = 520, ...) that does not include 1. The challenge is to identify whether a given number will continue indefinitely in a cycle or eventually reach the number 1.

# Input:
# A single integer n.

# Output:
# Return true if n is a Lucky Number, and false if not.

# Example 1:
# Input:
# n = 100

# Output:
# true

# Example 2:
# Input:
# n = 4

# Output:
# false

# Constraints:
# 1 <= n <= 10^4
# Your task is to implement the function isLuckyNumber(n) which will check for the Lucky Number property for the given input n.

def isLuckyNumber(n):
    def get_next_num(num):
        next_num = 0
        while num > 0:
            digit = num % 10
            next_num += digit ** 3
            num //= 10
        return next_num

    seen = set()
    while n not in seen:
        seen.add(n)
        n = get_next_num(n)
        if n == 1:
            return True
    return False

# Example usage:
print(isLuckyNumber(100))  # Output: True
print(isLuckyNumber(4))    # Output: False
