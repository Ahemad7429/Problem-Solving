# Sorted Array Search
# You are given a sorted array arr containing distinct integers. Your task is to implement a function search_position that, given a target value, returns the index where the target is found in the array. If the target is not present, return the index where it would be if inserted in order.

# Note:-
# Implement an algorithm with O(log n) runtime complexity.

# Input format:-
# arr (1 <= len(nums) <= 10^4) is a sorted array of distinct integers.<br>
# target (1 <= target <= 10^5) is the value to search for or insert.
# Output format1 :-
# Return an integer representing the index where the target is found or the index where it would be inserted.

# Examples
# Example 1
# Input: arr = [1,3,5,6], target = 5 
# Output: 2
# Example 2
# Input: arr = [1,3,5,6], target = 2
# Output: 1

class Solution:
    def search_position(self, arr, target):
      left, right = 0, len(arr) - 1
    
      while left <= right:
          mid = left + (right - left) // 2
          
          if arr[mid] == target:
              return mid
          elif arr[mid] < target:
              left = mid + 1
          else:
              right = mid - 1
      
      return left


# Sort Balls
# Given an array arr with n balls numbered 0, 1, or 2, sort them in place so that balls of the same number are adjacent, with the numbers in the order 0, 1, and 2.

# Note:-
# You must solve this problem without using the library's sort function.

# Input format:
# n == arr.length
# 1 <= n <= 200
# arr[i] is either 0, 1, or 2.

# Output format:
# You do not need to return anything, sort them in place.

# Examples
# Example 1
# Input: n=6 , arr = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2
# Input: n=5 , nums = [2,0,1,1,1]
# Output: [0,1,1,1,2]
    
class Solution:
    def sort_balls(self, nums):
      left, mid, right = 0, 0, len(nums) - 1
      
      while mid <= right:
          if nums[mid] == 0:
              nums[left], nums[mid] = nums[mid], nums[left]
              left += 1
              mid += 1
          elif nums[mid] == 1:
              mid += 1
          else:
              nums[mid], nums[right] = nums[right], nums[mid]
              right -= 1

# Maximum Element Frequency
# You are given an array a consisting of n integers. Your task is to find the frequency of the maximum element in the array.

# Input format
# The first line contains an integer n (1 ≤ n ≤ 10^5) — the size of the array.
# The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 10^9) — the elements of the array. You will be given a function to implement with parameters as array a and its length n.

# Output format
# Return a single integer — the frequency of the maximum element in the array.

# Examples
# Example 1
# Input

# 5
# 1 3 2 3 3
# Output

# 3
# Example 2
# Input

# 5 5 5 5 5 5
# Output

# 6
# Explanation
# In the first example, the maximum element is 3, and it appears 3 times in the array.
# In the second example, all elements are the same, and the maximum element (5) appears 6 times.
              
class Solution:
    def maxElementFrequency(self, n, a):
        max_elem = max(a)
        return a.count(max_elem)