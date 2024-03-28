# Even and Odd Digit Sums
# Write a program that takes an integer 'n' as input and prints the sum of all its even digits and the sum of all its odd digits separately. Digits refer to numbers, not places within the integer.

# Input Format:
# The input consists of a single integer 'n' on a single line.

# Output Format:
# The program outputs two space-separated integers on a single line:
# 1. The sum of all even digits in 'n'.
# 2. The sum of all odd digits in 'n'.
# Example:
# Input:
# 987654
# Output:
# 18 21
# Constraints:
# 0 <= n <= 10000
# Explanation:
# In the input integer 987654, the even digits are 8, 6, and 4. Their sum is 8 + 6 + 4 = 18 .

# The odd digits in the input are 9, 7, and 5. Their sum is 9 + 7 + 5 = 21.

# Therefore, the program outputs "18 21", where 18 is the sum of even digits and 21 is the sum of odd digits.

class Solution:
    def calculate_digit_sums(input):
      evenSum = 0
      oddSum = 0
      while input > 0:
         lastDigit = input % 10
         if(lastDigit % 2 == 0):
            evenSum += lastDigit
         else:
            oddSum += lastDigit
         input = int(input / 10)

      print(evenSum, end= " ")
      print(oddSum)
      
Solution.calculate_digit_sums(987654)