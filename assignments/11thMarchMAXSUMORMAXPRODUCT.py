# MAXSUM OR MAX PRODUCT
# A learner from heyCoch loves finding unique things, so in the next task by heyCoach,he has been assigned to check if in a given array say nums say s is the maximum sum out of all the subarray he can get from an array nums, and p is the maximum product he can get out of all subarrays, his task is to check if s is greater than p or not.
# if(s>p) print 1;
# if(s<p) print -1;
# if(s==p) print 0;

# Sample Input:
# 5

# 9 12 18 66 94
# Sample Output:
# -1

# Sample Input- 2
# 2
# -1 1
# Sample Output - 2
# 0

# Sample Input- 3
# 2
# 2 2
# Sample Output - 3
# 0

# Constraints:
# The length of the array nums will be between 1 and 10^5.

# For all 0<i<nums.length, -10^4<=nums[i]<=10^4.


def max_sum_or_max_product(nums):
    max_sum = float('-inf')
    max_product = float('-inf')
    
    # Calculate maximum sum
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    # Calculate maximum product
    current_product = 1
    for num in nums:
        current_product *= num
        max_product = max(max_product, current_product)
    
    # Compare max_sum and max_product
    if max_sum > max_product:
        return 1
    elif max_sum < max_product:
        return -1
    else:
        return 0

# Example usage:
nums1 = [9, 12, 18, 66, 94]
print(max_sum_or_max_product(nums1))  # Output: -1

nums2 = [-1, 1]
print(max_sum_or_max_product(nums2))  # Output: 0

nums3 = [2, 2]
print(max_sum_or_max_product(nums3))  # Output: 0
