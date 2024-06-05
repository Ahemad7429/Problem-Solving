# https://leetcode.com/problems/longest-common-prefix/description/

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Find the minimum length string from the array
    min_length = min(len(s) for s in strs)
    
    # Initialize the longest common prefix to an empty string
    longest_prefix = ""
    
    # Loop through each character index up to the length of the shortest string
    for i in range(min_length):
        # Get the character at the current index from the first string
        current_char = strs[0][i]
        
        # Check if this character is the same in all other strings
        if all(s[i] == current_char for s in strs):
            longest_prefix += current_char
        else:
            break
    
    return longest_prefix

# Test cases
print(longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog","racecar","car"]))    # Output: ""
