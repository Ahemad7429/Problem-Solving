# Positive Negative Alternate
# In a town, residents have a unique way of arranging numbers in arrays. They prefer to maintain an alternating pattern of Negative and positive numbers to create a harmonious sequence. However, sometimes they need a little help rearranging their arrays to achieve this pattern.

# Task

# As an assistant to the townspeople of Alternville, your task is to write a function that takes an array of integers as input and rearranges it to create an alternating pattern of negative and positive numbers. If there are more of one kind than other (meaning if there are more positive numbers or more negative numbers) you should move all the remaining to the end of the array and if there is a zero do not include it in the array.
# Also make sure that positive and negative numbers are sorted in their own individual group, for example, if the given array is [-1, 3,4,-6,2,5,9,-2] then the output should be: [-6,2,-2,3,-1,4,5,9]. The resulting array should start with the lowest number of the given array.

# Input

# An integer n (1 ≤ n ≤ 100), represents the number of elements in the array.
# A list of n integers, where each integer is in the range of -1000 to 1000 (inclusive).
# Output:

# A list of n integers, representing the rearranged array with an alternating begative-positive pattern.

# Sample Input:

# 5
# -9 11 4 6 -2
# Sample Output:

# -9 4 -2 6 11
# Sample Input:

# 7
# 0 -3 5 9 -4 10 -6
# Sample Output:

# -6 5 -4 9 -3 10 
# Note you don't have to include zeroes in result


class Solution:
    def alternatePandE(self, ar):
      arr = [x for x in ar if x != 0]
      
      positive_nums = sorted([x for x in ar if x > 0])
      negative_nums = sorted([x for x in ar if x < 0])
      
      result = []
      i, j = 0, 0
      
      while i < len(negative_nums) and j < len(positive_nums):
          result.append(negative_nums[i])
          result.append(positive_nums[j])
          i += 1
          j += 1
      
      while i < len(negative_nums):
          result.append(negative_nums[i])
          i += 1
      
      while j < len(positive_nums):
          result.append(positive_nums[j])
          j += 1

      print(" ".join(map(str, result)))