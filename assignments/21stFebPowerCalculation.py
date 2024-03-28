# Power Calculation
# Write a program that calculates the value of x^n , where 'x' and 'n' are integers taken as input from the user. You need to print the result of the calculation.

# Note: For this question, you can assume that 0^0 is equal to 1.

# Input Format:
# The input consists of two integers 'x' and 'n' on separate lines.

# Output Format:
# The program outputs the value of x^n as a single integer.

# Example:
# Input:
# 2
# 5
# Output:
# 32
# Constraints:
# -10^9 <= x <= 10^9
# 0 <= n <= 10^9
# Explanation:
# The value of 2^5 is calculated as 2 x 2 x 2 x 2 x 2 = 32 , which is printed as the output of the program.


class Solution:
    @staticmethod
    def power(x, n):
        return x ** n

# Example usage:
result = Solution.power(2, 3)
print(result)  # Output: 8
