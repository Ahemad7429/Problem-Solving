# k different pairs
# Given an array of integers nums and an integer k, write a program to return the number of unique k-diff pairs in the array.
# A k-diff pair is defined as an integer pair (nums[i], nums[j]), where the following conditions are true:

# 0≤i,j<length of nums and i≠j.

# The absolute difference between the two numbers is exactly k, i.e., ∣nums[i]−nums[j]∣=k.

# Input Format:
# The first line contains an integer n and k space-separated, representing the number of elements in the array nums.

# The second line contains n space-separated integers, the elements of the array nums.

# Output Format:
# Print a single integer representing the number of unique k-diff pairs in the array.

# Sample Input:
# 5 2
# 3 1 4 1 5  

# Sample Output:
# 2

# Explanation:
# In the given array, there are two unique pairs that have a difference of 2: the pair (1, 3) and the pair (3, 5). Hence, the output is 2.

# Constraints:
# The number of elements in the array nums is within the range [1,10^4].

# The value of each element in nums is in the range [−10^7 ,10^7].

# k is a non-negative integer within the range [0,10^7].


def find_pairs(nums, k):
    if k < 0:
        return 0

    seen = set()
    pairs = set()

    for num in nums:
        if num + k in seen:
            pairs.add((num, num + k))
        if num - k in seen:
            pairs.add((num - k, num))
        seen.add(num)
    
    return len(pairs)

# Read input
n, k = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))

# Find and print the number of unique k-diff pairs
result = find_pairs(nums, k)
print(result)