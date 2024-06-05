# Help the governor
# RBI wants to introduce currency of new denominations,so for this, the Governor conducts a poll about the among N banks. Governor imposed a restriction on the denomination of the currency that is the denomination can be in the range of ==[1,N]==.Votes of all the banks have been stored in the votes array and the RBI will release currency of only those denominations which have got more than 1 vote. So you have been provided with the votes array and you need to return the array which will contain the denominations of the currency which is going to be released by the RBI sorted in increasing order. If no denominations got more than 1 vote then simply return an empty array.

# Note: Can you wirte an algorithm that runs in O(N) Time complexity and O(1) space complexity if we exclude the space used by the answer array?

# Example 1
# Input
# votes = [4,3,2,1,2,1]
# Output
# [1,2]
# Explanation:
# Currency of denominations 1 and 2 got more than 1 vote so they are going to be released by the RBI

# Example 2
# Input

# votes = [3,4,3,1]
# Output
# [3]
# Explanation:
# only currency of denomination 3 got more than 1 vote.

# Constraints:
# 1 <= n= 10000
# 1 <= votes[i] <= N

def findCurrency(votes): 
    n = len(votes)
    count = {}

    # Count the occurrences of each denomination
    for vote in votes:
        if vote in count:
            count[vote] += 1
        else:
            count[vote] = 1

    released_denominations = []

    # Check if each denomination received more than one vote
    for denom, freq in count.items():
        if freq > 1 and abs(denom) <= n:
            released_denominations.append(abs(denom))

    # Sort the released denominations in increasing order
    released_denominations.sort()

    return released_denominations



# Range of an array
# Given an unsorted array arr of n non-negative integers, you have to find the range of an array. The range of an array is the difference between the maximum and minimum value of the array. If a single value is present return 0.

# Example 1
# Input
# arr = [3,2,10,4,7,8]
# Output
# 8
# Explanation:
# The Maximum value in the array is 10 and the minimum value is 2 so the range is 10 - 2 = 8

# Example 2
# Input
# arr = [30,15,6,10,12,22]
# Output
# 24
# Explanation:
# The Maximum value in the array is 30 and the minimum value is 6 so the range is 30 - 6 = 24

# Constraints:
# 0 < n <= 100000
# 0 <= arr[i] <= 100000

class Solution:
    def rangeOfAnArray(self, arr):
      min_val = float('inf')
      max_val = 0
      for ele in arr:
        if (ele > max_val):
          max_val = ele
      
        if (ele < min_val):
          min_val = ele

      return max_val - min_val
    

# Only K Strings
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).

# For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
# You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.

# Input Format:

# First line takes a string 's' as input which represents the sentence which is to be truncated.

# Second line takes an integer 'k' as input which denotes the the first k​​​​​​ words that are to be truncated from s.

# Output format:

# Return s​​​​​​ after truncating it.

# Example 1
# Input
#  s = "Hello how are you Contestant", k = 4
# Output
# "Hello how are you"
# Explanation -
# The words in s are ["Hello", "how" "are", "you", "Contestant"]. The first 4 words are ["Hello", "how", "are", "you"]. Hence, you should return "Hello how are you".

# Example 2
# Input
#  s = "What is the solution to this problem", k = 4
# Output
# "What is the solution"
# Explanation -
# The words in s are ["What", "is" "the", "solution", "to", "this", "problem"]. The first 4 words are ["What", "is", "the", "solution"]. Hence, you should return "What is the solution".

# Constraints: 1<=k<=length of string s<=100
    
class Solution:
    def onlyKString(self, s, k):
      words = []
      word = ""
      for ch in s:
        if(ch == " "):
          words.append(word)
          word = ""
        else:
          word += ch

        if(len(words) == k):
          return " ".join(words)