# Odd Even Alternative
# You are given an array of integers of length N. Your task is to rearrange the numbers in such a way that the resulting array follows an alternate odd-even pattern.
# In other words, the first number in the rearranged array should be odd if the smallest element is odd, and the first number should be even if the smallest element is even. Subsequently, the second number should be even if the first number is odd, and the second number should be odd if the first number is even. This pattern continues alternately throughout the array.

# Additionally, the groups of odd and even numbers should be individually sorted in the resulting array. For example, if the given array is [2,9,5,13,8,12], and the smallest element is 2 (which is even), then the output should be [2,5,8,9,12,13], following the even-odd pattern and sorting the even and odd numbers separately.

# Input Format:
# The first line of input contains an integer N (1 ≤ N ≤ 10^5), representing the length of the array.
# The second line of input contains N space-separated integers A1, A2, ..., AN (-10^9 ≤ Ai ≤ 10^9), representing the elements of the array.
# Output Format:
# If it is possible to rearrange the array to achieve the alternate odd-even pattern while sorting the odd and even numbers individually, output the rearranged array on a single line, separated by spaces.

# If it is not possible, output "Not Possible".

# Sample Input:
# 6

# 2 9 5 13 8 12
# Sample Output:
# 2 5 8 9 12 13
# Sample Input:
# 6

# 1 11 7 2 8 16
# Sample Output:
# 1 2 7 8 11 16
# Sample Input:
# 2
# 2 4
# Sample Output:
# Not Possible
# Constraints:
# The input array will always contain at least one odd and one even number.
# The length of the array will not exceed 10^5.
# The elements of the array can range from -10^9 to 10^9.


class Solution:
    def odd_even_alternating(A):
      A.sort()
      
      odd_nums = [x for x in A if x % 2 != 0]
      even_nums = [x for x in A if x % 2 == 0]
      
      if A[0] % 2 == 0:
          start_with_even = True
      else:
          start_with_even = False
      
      if abs(len(odd_nums) - len(even_nums)) > 1:
          return "Not Possible"
      
      result = []
      if start_with_even:
          i, j = 0, 0
          while i < len(even_nums) and j < len(odd_nums):
              result.append(even_nums[i])
              i += 1
              result.append(odd_nums[j])
              j += 1
          while i < len(even_nums):
              result.append(even_nums[i])
              i += 1
          while j < len(odd_nums):
              result.append(odd_nums[j])
              j += 1
      else:
          i, j = 0, 0
          while i < len(odd_nums) and j < len(even_nums):
              result.append(odd_nums[i])
              i += 1
              result.append(even_nums[j])
              j += 1
          while i < len(odd_nums):
              result.append(odd_nums[i])
              i += 1
          while j < len(even_nums):
              result.append(even_nums[j])
              j += 1
  
      return " ".join(map(str, result))