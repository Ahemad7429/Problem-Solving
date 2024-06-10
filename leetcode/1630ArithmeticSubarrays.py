# https://leetcode.com/problems/arithmetic-subarrays/description/

def checkArithmeticSubarrays(nums, l, r):
    def isArithmetic(arr):
        if len(arr) < 2:
            return False
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True

    result = []
    for i in range(len(l)):
        subarray = nums[l[i]:r[i] + 1]
        result.append(isArithmetic(subarray))

    return result

# Example usage
nums1 = [4, 6, 5, 9, 3, 7]
l1 = [0, 2, 2]
r1 = [2, 5, 4]
print(checkArithmeticSubarrays(nums1, l1, r1))  # Output: [True, False, True]

nums2 = [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10]
l2 = [0, 1, 6, 4, 8, 7]
r2 = [4, 4, 9, 7, 9, 10]
print(checkArithmeticSubarrays(nums2, l2, r2))  # Output: [False, True, False, False, True, True]
