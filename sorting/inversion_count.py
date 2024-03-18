# Special Pair of Scores
# You are given an array of integers representing the performance scores of n participants in a coding competition. Each participant is assigned a unique score based on their performance, and no two participants have the same score. Your task is to calculate the total number of Special pairs in the list of scores.
# A Special pair is defined as a pair of indices (i, j) such that i < j and scores[i] > scores[j].

# Sample Input:
# 6

# 8 4 2 1 5 3
# Output:
# 10


class Solution:
    @staticmethod
    def inversion_count(arr, n):
      pairs = []
      for i in range(n-1):
         j = i + 1
         while (j < n):
            if(arr[i] > arr[j]):
                pairs.append((arr[i], arr[j]))
            j+=1
      print(pairs)
      print(len(pairs))
      
Solution.inversion_count([8, 4, 2, 1, 5, 3], 6)