# Minimum window substring
# Problem Statement:

# Develop an algorithm to identify the shortest contiguous substring in string s that encompasses all the characters present in string t, considering duplicates as well. If no such substring can be found, the solution should return an empty string.

# Note that the provided test cases will guarantee the presence of a single, unique solution.

# Input :

# s (String): The input string where the algorithm searches for the shortest contiguous substring.
# t (String): The target string containing characters to be present in the substring.
# Output : Return the shortest contiguous substring of s that encompasses all the characters present in t, considering duplicates.

# Example :

# s = "ADOBECODEBANC"
# t = "ABC"
# Output:

# "BANC"
# Constraints:

# m == s.length

# n == t.length

# 1 <= m, n <= 10^5

# s and t consist of uppercase and lowercase English letters.


from collections import Counter

class Solution:
    def minWindow(self, s, t):
      if not s or not t:
          return ""
  
      target_count = Counter(t)
      required_chars = len(target_count)
      formed_chars = 0
  
      window_count = {}
      left, right = 0, 0
      min_window = float("inf")
      min_window_start = 0
  
      while right < len(s):
          while right < len(s) and formed_chars < required_chars:
              char = s[right]
              window_count[char] = window_count.get(char, 0) + 1
              if char in target_count and window_count[char] == target_count[char]:
                  formed_chars += 1
              right += 1
  
          while left < right and formed_chars == required_chars:
              if right - left < min_window:
                  min_window = right - left
                  min_window_start = left
  
              char = s[left]
              window_count[char] -= 1
              if char in target_count and window_count[char] < target_count[char]:
                  formed_chars -= 1
              left += 1
  
      return "" if min_window == float("inf") else s[min_window_start:min_window_start + min_window]