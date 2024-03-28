# Check Common Digit in Range
# Write a program that takes two integer values within a specified range as input and returns true if there is a common digit in both numbers.
# A common digit refers to any digit that is present in both numbers.

# Input Format:
# The input consists of two integer values, num1andnum2, separated by spaces. Both num1andnum2 should be within the specified range.

# Output Format:
# The program outputs either "true" if there is a common digit in both numbers or "false" otherwise.

# Sample Input:
# 79 67
# Sample Output:
# true
# Constraints:
# The range of input integers is from 0 to 1000 (inclusive).
# Both num1andnum2 are within this range.
# Explanation:
# First number is 35 and the second number is 45. Both numbers have the common digit 5, so the program outputs "true" indicating that there is a common digit in both numbers.


class Solution:
    def check_common_digit(num1, num2):
        count = 0
        freq1 = [0] * 10 
        freq2 = [0] * 10 

        while num1 > 0:
            freq1[num1 % 10] += 1
            num1 = int(num1 / 10)
        
        while num2 > 0:
            freq2[num2 % 10] += 1
            num2 = int(num2 / 10)

        for i in range(10):
         
            if (freq1[i] > 0 and freq2[i] > 0):
                count += 1
        return count

print(Solution.check_common_digit(45,57))