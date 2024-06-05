# ROHAN LOVES 0 (1)
# Rohan loves 0, he has been assigned a task by his coach to check whether is it possible to find a subarray in the array nums, with sum 0 in it. Rohan thinks that this task is quite easy as he know the brute-force method, but his coach has strictly instructed to think of a optimized approach for the above problem as brute force will not work this time.

# Hint: Prefix Sum Prefix Sum[i] is defined as the sum of all the values of the array up to index i.

# PrefixSum[0] = nums[0];

# PrefixSum[1] = nums[0]+nums[1];

# PrefixSum[i] = nums[0]+nums[1]+nums[2]+........nums[i].

# Sample Input:

# 7

# 1 4 -2 -2 5 -4 3

# Sample Output:

# Yes

# Constraints :

# 1<=nums.length()<=10^4;

# -10^4<=nums[i]<=10^4;

def has_zero_sum_subarray(nums):
    prefix_sum = 0
    prefix_sum_set = set()
    
    for num in nums:
        prefix_sum += num
        if prefix_sum == 0 or prefix_sum in prefix_sum_set:
            return "Yes"
        prefix_sum_set.add(prefix_sum)
    
    return "No"

# Example usage
nums = [1, 4, -2, -2, 5, -4, 3]
print(has_zero_sum_subarray(nums))  # Output: Yes

nums = [1, 2, 3, 4, 5]
print(has_zero_sum_subarray(nums))  # Output: No
