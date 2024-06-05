class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        start = 0
        max_length = 0
        
        for i, char in enumerate(s):
            if char in last_index and last_index[char] >= start:
                start = last_index[char] + 1
            last_index[char] = i
            max_length = max(max_length, i - start + 1)
        
        return max_length