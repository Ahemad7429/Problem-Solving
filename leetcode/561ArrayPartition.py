# https://leetcode.com/problems/array-partition/description/

def arrayPairSum(nums):
    nums.sort()
    return sum(nums[i] for i in range(0, len(nums), 2))
