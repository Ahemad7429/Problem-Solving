# SOLO SUM
# Ramesh is working on a problem given by his teacher, the problem states that he is given an array(say nums),

# He has to find such an array (say ans) such that ans[i]=leftsum[i]+rightsum[i]. Help Ramesh to solve the problem. leftsum[i] is the sum of all the elements to the left of index i in the array nums, if there is no such element leftsum[i]=0;

# rightsum[i] is the sum of all the elements to the right of index i in the array nums, if there is no such element rightsum[i]=0;

# Example 1
# Input:
# nums = [1, 2, 3, 4, 5]
# Output:
# [14, 13, 12, 11, 10]
# Example 2
# Input
# nums =[1, 2, -3, 4, -5]
# Output:
# [-2, -3, 2, -5, 4]
# Constraints :
# 1 <= nums.length <= 1000

# -10000 <= nums[i] <= 10000

def left_right_sum(nums):
    left, right = 0, sum(nums)
    ans = []
    for x in nums:
        right -= x
        ans.append(left + right)
        left += x
    return ans

print(left_right_sum([1, 2, 3, 4, 5]))
print(left_right_sum([1, 2, -3, 4, -5]))