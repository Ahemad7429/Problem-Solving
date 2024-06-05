# Hashmap Implementation
# "Given below array of integers, your task is to simply implement map storing each number and its frequency and returning it.

# Input:
# Given a vector of size n.

# output:
# Print each number with its frequency in sorted fo.

# Example:
# input: n=6, arr={1, 2, 4, 1, 3, 3}
# output: [1,2] [2,1] [3,2] [4,1]

class Solution:
    def map_implementation(self, arr):
        frequency = {}

        for ele in arr:
            if ele in frequency:
                frequency[ele] += 1
            else:
                frequency[ele] = 1

        sorted_frequency = sorted(frequency.items())

        for key, value in sorted_frequency:
            print("[{}, {}]".format(key, value), end=" ")
        
     
    
Solution().map_implementation([1,2,3,4,5])