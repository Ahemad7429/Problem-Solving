# https://leetcode.com/problems/3sum/description/

def threeSum(nums):
    nums.sort()  # Step 1: Sort the array
    result = []
    length = len(nums)
    
    for i in range(length - 2):
        # Skip duplicate elements for the first element of the triplet
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, length - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicate elements for the second and third elements of the triplet
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
                
            elif total < 0:
                left += 1
            else:
                right -= 1
                
    return result

# Example usage:
print(threeSum([-1,0,1,2,-1,-4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
