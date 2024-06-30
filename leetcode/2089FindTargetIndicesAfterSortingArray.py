# https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

class Solution:
    def targetIndices(self, nums, target):
        sorted_nums = sorted(nums)
        indices = []
        for i, num in enumerate(sorted_nums):
            if num == target:
                indices.append(i)
        return indices