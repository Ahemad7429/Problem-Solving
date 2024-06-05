# LongestSubStringWith K unique charachters
# Given a string S and an integer K, find the length of the longest substring of S that contains exactly K unique characters. If no such substring exists, return -1.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function longestKSubstr() which takes the string S and an integer K as input and returns the length of the longest substring with exactly K distinct characters. If there is no substring with exactly K distinct characters then return -1.
# Input:

# A string S containing lowercase letters.
# An integer K, the number of unique characters required in the substring.
# Output:

# The length of the longest substring with exactly K unique characters.
# Constraints:

# 1<=length of S<=10^6
# 0<= K<= 26
# Examples:

# Input:
# S = "aabacbebebe", K = 3

# Output:
# 7

# Explanation:
# The longest substring with exactly 3 distinct characters is "cbebebe".

def longestKSubstr(s, k):
    if k == 0 or len(s) == 0:
        return -1

    char_count = {}
    left = 0
    max_length = -1

    for right in range(len(s)):
        # Add the character at the current position to the hashmap
        if s[right] in char_count:
            char_count[s[right]] += 1
        else:
            char_count[s[right]] = 1

        # If the number of unique characters in the current window exceeds k, shrink the window from the left
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        # If the current window has exactly k unique characters, update the maximum length
        if len(char_count) == k:
            max_length = max(max_length, right - left + 1)

    return max_length

# Example usage:
S = "aabacbebebe"
K = 3
print(longestKSubstr(S, K))  # Output: 7