# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/submissions/1281453831/

def minPairSum(nums):
    # Sort the array
    nums.sort()
    
    # Initialize pointers
    left = 0
    right = len(nums) - 1
    
    # Initialize the maximum pair sum
    max_pair_sum = 0
    
    # Form pairs from the ends towards the middle
    while left < right:
        # Calculate the pair sum
        pair_sum = nums[left] + nums[right]
        
        # Update the maximum pair sum
        max_pair_sum = max(max_pair_sum, pair_sum)
        
        # Move pointers
        left += 1
        right -= 1
    
    return max_pair_sum

# Example usage
print(minPairSum([3, 5, 2, 3]))  # Output: 7
print(minPairSum([3, 5, 4, 2, 4, 6]))  # Output: 8
