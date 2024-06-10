# MAX FREEQUENCY ELEMENTS SUM
# Nitin has just joined a heyCoach training program, he has been assigned to solve the following problem,
# given an integer array (say nums), he has been asked to provide the sum of the array elements which has maximum frequency.

# Example 1
# Input
# nums = [1, 2, 3, 3, 3, 2, 2, 5]

# Output:
# 5

# Explanation:
# only elements 3 & 2 has maximum frequency(3),

# Example 2
# Input:
# nums = [7,6,5,8,9]

# Output:
# 35

# Constraints:
# 1<=nums.length<=1000

# For all 0<= i <nums.length, -1000<=nums[i]<=1000


def max_frequency_element_sum(nums):
    frequency_map = {}
    
    # Count the frequency of each element
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1
    
    max_frequency = max(frequency_map.values())  # Find the maximum frequency
    
    # Calculate the sum of elements with maximum frequency
    max_frequency_sum = sum(num for num, freq in frequency_map.items() if freq == max_frequency)
    
    return max_frequency_sum

# Example usage:
nums1 = [1, 2, 3, 3, 3, 2, 2, 5]
print(max_frequency_element_sum(nums1))  # Output: 5

nums2 = [7, 6, 5, 8, 9]
print(max_frequency_element_sum(nums2))  # Output: 35


