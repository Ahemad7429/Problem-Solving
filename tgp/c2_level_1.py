# Reduce Sum
# You are given an array nums of positive integers. In one operation, you can choose any number from nums and reduce it to exactly half the number. (Note that you may choose this reduced number in future operations.)

# Return the minimum number of operations to reduce the sum of nums by at least half.

# Example 1
# Input
# nums = [5,19,8,1]
# Output
# 3
# Explanation:
# The initial sum of nums is equal to 5 + 19 + 8 + 1 = 33. The following is one of the ways to reduce the sum by at least half: Pick the number 19 and reduce it to 9.5. Pick the number 9.5 and reduce it to 4.75. Pick the number 8 and reduce it to 4. The final array is [5, 4.75, 4, 1] with a total sum of 5 + 4.75 + 4 + 1 = 14.75. The sum of nums has been reduced by 33 - 14.75 = 18.25, which is at least half of the initial sum, 18.25 >= 33/2 = 16.5. Overall, 3 operations were used so we return 3. It can be shown that we cannot reduce the sum by at least half in less than 3 operations.

# Example 2
# Input
# nums = [3,8,20]
# Output
# 3
# Explanation:
# The initial sum of nums is equal to 3 + 8 + 20 = 31. The following is one of the ways to reduce the sum by at least half: Pick the number 20 and reduce it to 10. Pick the number 10 and reduce it to 5. Pick the number 3 and reduce it to 1.5. The final array is [1.5, 8, 5] with a total sum of 1.5 + 8 + 5 = 14.5. The sum of nums has been reduced by 31 - 14.5 = 16.5, which is at least half of the initial sum, 16.5 >= 31/2 = 16.5. Overall, 3 operations were used so we return 3. It can be shown that we cannot reduce the sum by at least half in less than 3 operations.

# Constraints:
# 1 <= nums.length <= 10^5

# 1 <= nums[i] <= 10^7


# import heapq

# class Solution:
#     def minOperations(self, nums):
#         # Convert to a max-heap (by storing negative values)
#         max_heap = [-num for num in nums]
#         heapq.heapify(max_heap)
        
#         # Calculate the initial sum
#         initial_sum = sum(nums)
#         current_sum = initial_sum
#         target_sum = initial_sum / 2
        
#         # Counter for the number of operations
#         operations = 0
        
#         # Keep reducing the sum until it's at least halved
#         while current_sum > target_sum:
#             # Extract the largest element (in negative form, so we negate it)
#             largest = -heapq.heappop(max_heap)
#             half = largest / 2
#             current_sum -= half
            
#             # Push the halved value back into the heap
#             heapq.heappush(max_heap, -half)
            
#             # Increment the number of operations
#             operations += 1
        
#         return operations

# # Test the solution
# solution = Solution()
# print(solution.minOperations([5, 19, 8, 1]))  # Output: 3
# print(solution.minOperations([3, 8, 20]))    # Output: 3


# Triangle Sum
# You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 inclusive.

# The triangular sum of nums is the value of the only element present in nums after the following process terminates:

# Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1. For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator. Replace the array nums with newNums. Repeat the entire process starting from step 1. Return the triangular sum of nums.

# Example 1
# Input
# nums = [1,2,3,4,5]
# Output
# 8
# Explanation:
# The above diagram depicts the process from which we obtain the triangular sum of the array.

# Image

# Example 2
# Input
#  [5]
# Output
# 5
# Explanation:
# Since there is only one element in nums, the triangular sum is the value of that element itself.

class Solution:
    def triangularSum(self, nums):
        while len(nums) > 1:
            newNums = []
            for i in range(len(nums) - 1):
                newNums.append((nums[i] + nums[i + 1]) % 10)
            nums = newNums
        return nums[0]

# Test the solution
solution = Solution()
print(solution.triangularSum([1, 2, 3, 4, 5]))  # Output: 8
print(solution.triangularSum([5]))              # Output: 5


# Minimum Non-Zero Product of the Array Elements
# You are given a positive integer p. Consider an array nums (1-indexed) that consists of the integers in the inclusive range [1, 2p - 1] in their binary representations. You are allowed to do the following operation any number of times:

# Choose two elements x and y from nums. Choose a bit in x and swap it with its corresponding bit in y. Corresponding bit refers to the bit that is in the same position in the other integer. For example, if x = 1101 and y = 0011, after swapping the 2nd bit from the right, we have x = 1111 and y = 0001.

# Find the minimum non-zero product of nums after performing the above operation any number of times. Return this product modulo 10^9 + 7.

# Note: The answer should be the minimum product before the modulo operation is done.
# Input Format:

# A single integer p which makes up the array nums.

# Output format:

# Return a single integer representing the minimum non zero product of nums.

# Example 1
# Input
# p = 2
# Output
# 6
# Explanation:
# nums = [01, 10, 11]. Any swap would either make the product 0 or stay the same. Thus, the array product of 1 * 2 * 3 = 6 is already minimized.

# Example 2
# Input
# p=3
# Output
# 1512
# Explanation:
# nums = [001, 010, 011, 100, 101, 110, 111]

# In the first operation we can swap the leftmost bit of the second and fifth elements.
# The resulting array is [001, 110, 011, 100, 001, 110, 111].
# In the second operation we can swap the middle bit of the third and fourth elements.
# The resulting array is [001, 110, 001, 110, 001, 110, 111]. The array product is 1 * 6 * 1 * 6 * 1 * 6 * 7 = 1512, which is the minimum possible product.
# Constraints:
# 1 <= p <= 60

class Solution:
    def __init__(self):
        self.mod = 10**9 + 7
      
    def power_mod(self, base, exp):
        result = 1
        base = base % self.mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % self.mod
            exp = exp >> 1
            base = (base * base) % self.mod
        return result
    
    def minNonZeroProduct(self, p):
        if p == 1:
            return 1
        max_num = (1 << p) - 1
        second_max_num = max_num - 1
        num_occurrences = (1 << (p - 1)) - 1
        
        product = self.power_mod(second_max_num, num_occurrences)
        product = (product * max_num) % self.mod
        
        return product
