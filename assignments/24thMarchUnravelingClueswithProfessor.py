# Unraveling Clues with Professor
# Professor Prateek from HeyCoach coding academy in Bangalore challenges Varshil to find all indices where a given pattern appears within a given text. Both text and pattern consist of lowercase alphabetical characters. The goal is to identify the starting indices in the text where the complete pattern is found.

# Input Format:

# The first line contains the string text, consisting of lowercase alphabetical characters (1 <= |text| <= 10^5).
# The second line contains the string pattern, consisting of lowercase alphabetical characters (1 <= |pattern| <= 10^5).
# Output Format:

# A list of integers separated by spaces, representing the starting indices of the text where the pattern appears in its entirety.
# Constraints:

# 1 <= |text| <= 10^5
# 1 <= |pattern| <= 10^5
# The text and pattern consist only of lowercase alphabetical characters.
# Example:

# Input:
# text = "ababcabab"
# pattern = "ab"
# Output:
# 0 2 5 7
# Explanation:

# The pattern "ab" appears at indices 0, 2, 5, and 7 within the text.

class Solution:
  def findPatternIndices(self, text, pattern):
    indices = []
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        found = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                found = False
                break
        if found:
            indices.append(i)
    
    return indices