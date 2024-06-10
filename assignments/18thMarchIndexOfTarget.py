# Index of target
# You have been given a sorted and rotated array containing distinct integers. The rotation point is unknown, and it splits the array into two sorted subarrays. Your task is to find a target integer within this rotated array and return its index if it exists. If the target integer is not present, you should return -1.

# Your algorithm must solve this problem with a runtime 
# complexity of O(log n).
# Sample Input 

# 7
# 4 5 6 7 0 1 2 
# 0
# Sample Output

# 4
# Constraints:

# 1 <= nums.length <= 5000

# -104 <= nums[i] <= 104

# All values of nums are unique.

# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

def search(nums, target):
    if not nums:
        return -1

    left, right = 0, len(nums) - 1

    # Find the pivot point
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    pivot = left

    # Determine which side to search
    left, right = 0, len(nums) - 1
    if nums[pivot] <= target <= nums[right]:
        left = pivot
    else:
        right = pivot - 1

    # Standard binary search
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Test the solution
print(search([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4
print(search([4, 5, 6, 7, 0, 1, 2], 3))  # Output: -1
