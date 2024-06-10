# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

def smallerNumbersThanCurrent(nums):
    # Pair each number with its index
    sorted_nums = sorted((num, i) for i, num in enumerate(nums))
    
    # Dictionary to hold the count of smaller numbers
    smaller_count = {}
    
    # Initialize the count
    count = 0
    
    # Iterate through the sorted numbers
    for i, (num, original_index) in enumerate(sorted_nums):
        # If the number is not in the dictionary, it's the first time we see this number
        if num not in smaller_count:
            smaller_count[num] = i  # i is the number of smaller elements before this number
    
    # Construct the result using the dictionary
    result = [smaller_count[num] for num in nums]
    
    return result

# Example usage
print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))  # Output: [4, 0, 1, 1, 3]
print(smallerNumbersThanCurrent([6, 5, 4, 8]))     # Output: [2, 1, 0, 3]
print(smallerNumbersThanCurrent([7, 7, 7, 7]))     # Output: [0, 0, 0, 0]
