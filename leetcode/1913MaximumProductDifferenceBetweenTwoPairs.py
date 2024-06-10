# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/

def maxProductDifference(nums):
    # Sort the array
    nums.sort()
    
    # The two largest numbers are the last two in the sorted array
    max1, max2 = nums[-1], nums[-2]
    
    # The two smallest numbers are the first two in the sorted array
    min1, min2 = nums[0], nums[1]
    
    # Calculate the product difference
    product_difference = (max1 * max2) - (min1 * min2)
    
    return product_difference

# Example usage
print(maxProductDifference([5, 6, 2, 7, 4]))  # Output: 34
print(maxProductDifference([4, 2, 5, 9, 7, 4, 8]))  # Output: 64
