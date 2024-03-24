# Can you move two's?
# Given an integer array nums, move all 2's to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array.

# You don't need to return anything in the function just perform inplace operations.

# Example
# Input :
# arr = [2,2,1]

# Output :
# [1,2,2]

# Constraints:
# 1 <= arr.length <= 4 * 10^4

# 0 <= arr[i] <= 10^9


class Solution:
    def movetwos(self, nums):
        j = -1
        for i in range(len(nums)):
            if(nums[i] == 2):
                j = i
                break
    
        for i in range(j+1, len(nums)):
            if(nums[i] != 2):
                nums[i], nums[j] = nums[j], nums[i]

        print(nums)

    def pushTwoToEnd(self, arr): 
        count = 0
        for i in range(len(arr)): 
            if arr[i] != 2: 
                arr[count] = arr[i] 
                count+=1
        
        while count < len(arr): 
            arr[count] = 2
            count += 1

        print(arr)

sol = Solution()
sol.pushTwoToEnd([2,2,1])