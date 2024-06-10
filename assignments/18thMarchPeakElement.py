# Peak Element
# Imagine you're a coach of a competitive programming team, and you've been given an interesting problem to solve. Your task is to help your team members find the index of the greatest peak element in an array. A peak element in an array is an element that is greater than or equal to its neighbours. To clarify, an element at the edge of the array only needs one neighbour to be considered a peak. For example, in the array [5, 3, 4], both 5 and 4 are peak elements.

# Sample Input 1

# 4
# 1 2 3 1
# Sample Output : 2 (the index of 3 is 2)
# Sample Input 2

# 5
# 1 7 3 5 9
# Sample Output : 4 (The index of 9 is 4)
# Constraints :

# The length of the array nums will be between 1 and 10^5.

# 0<i<nums.length

# -10^4<=nums[i]<=10^4.

def findPeakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

# Test the solution
print(findPeakElement([1, 2, 3, 1]))  # Output: 2 (index of 3)
print(findPeakElement([1, 7, 3, 5, 9]))  # Output: 4 (index of 9)
