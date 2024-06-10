# Maximum Deliciousness
# You're invited to a delicious banquet with n delectable dishes represented by their bitwise representation (numbers between 1 and 10^9). However, some dishes are hidden under silver cloches (k operations allowed). You can lift a cloche and double the bitwise representation of one hidden dish under it. Your goal is to maximize the overall "deliciousness" of the feast, measured by the bitwise OR of all dish values after lifting cloches.

# Input:
# n: Number of dishes (integers) - Integer between 1 and 10^5 (inclusive).
# nums: Array of dish bitwise representations - Integers between 1 and 10^9 for each dish in the 0-based index of nums.
# k: Number of cloches you can lift - Integer between 1 and 15 (inclusive).
# Output:
# max_deliciousness: The maximum possible bitwise OR of all dish values after lifting cloches at most k times.

# Example 1:
# Input:
# n = 2, nums = [12, 9], k = 1

# Output:
# 30 (Explanation: Lift the cloche on dish 1 to get [12, 18]. Then, max_deliciousness = 12 | 18 = 30)

# Example 2:
# Input:
# n = 3, nums = [8, 1, 2], k = 2

# Output:
# 35 (Explanation: Lift the cloche on dish 0 twice to get [32, 1, 2].
# Then, max_deliciousness = 32 | 1 | 2 = 35).

# Constraints:
# n: Number of dishes (integers) must be an integer between 1 and 10^5 (inclusive).
# nums: Array of dish bitwise representations must have a length equal to n. Each element in nums must be an integer between 1 and 10^9 (inclusive).
# k: Number of cloches you can lift must be an integer between 1 and 15 (inclusive).

def max_deliciousness(n, nums, k):
    # Function to calculate bitwise OR of a list
    def bitwise_or(lst):
        result = 0
        for num in lst:
            result |= num
        return result

    # Calculate the initial bitwise OR of all dishes
    initial_or = bitwise_or(nums)
    
    max_or = initial_or
    
    # Simulate doubling operations for each dish
    for i in range(n):
        current = nums[i]
        temp_nums = nums[:]
        
        for _ in range(k):
            current *= 2
            temp_nums[i] = current
            current_or = bitwise_or(temp_nums)
            max_or = max(max_or, current_or)
    
    return max_or

# Example usage:
n = 2
nums = [12, 9]
k = 1
print(max_deliciousness(n, nums, k))  # Output: 30

n = 3
nums = [8, 1, 2]
k = 2
print(max_deliciousness(n, nums, k))  # Output: 35

# Power of 4 or not.
# Given a number N, check if N is power of 4 or not.

# Input:
# N, number to find power of 4 or not.

# Output:
# return 1 of true else 0.

# Sample Input:
# 16

# Sample Output:
# 1

# Explanation:
# 4*4 = 4^2 =16 is expressed in terms of power of 4.


def isPowerOfFour( n: int) -> int:
      if n <= 0:
          return 0
      
      if n & (n - 1) != 0:
          return 0
      
      if n % 4 == 0:
          return 1
      
      return 0

# Example usage:
N = 16
print(isPowerOfFour(N))  # Output: 1

N = 8
print(isPowerOfFour(N))  # Output: 0

N = 64
print(isPowerOfFour(N))  # Output: 1

N = 256
print(isPowerOfFour(N))  # Output: 1

N = 32
print(isPowerOfFour(N))  # Output: 0


# Flip Bit
# Given an integer x and you can flip exactly one bit from 0 to 1. Write code to find the length of the longest contiguous subsegment of 1 you can create in the binary format.

# Input Format:
# A single line that contains an integer x.

# Output Format:
# A single line that contains an integer which represents the length of the longest contiguous subsegment of 1 you can create in the binary format.

# Example 1
# Input:
# 1775

# Output:
# 8

# Explanation:
# Binary of 1775 is 11011101111. So 4th bit(0 based indexed) from right can be flipped to get the contiguous subsegment of length 8.

# Example 2:
# Input:
# 7

# Output:
# 3

# Explanation:
# Binary of 7 is 111. So it doesn't have any bit 0 which can be flipped.

# Constraints:
# 0 <= x <= 10^18

def flip_bit_to_win(x):
    # Convert x to binary string without '0b' prefix
    binary_str = bin(x)[2:]
    
    # Split by '0' to get lengths of consecutive '1' segments
    segments = binary_str.split('0')
    
    # If there's no '0' in the binary representation, return the length of the whole binary string
    if len(segments) == 1:
        return len(binary_str)
    
    # Otherwise, calculate the maximum length possible by flipping one '0'
    max_length = 0
    
    for i in range(len(segments) - 1):
        # Length by flipping the zero between segments[i] and segments[i+1]
        combined_length = len(segments[i]) + 1 + len(segments[i + 1])
        max_length = max(max_length, combined_length)
    
    return max_length

# Example usage:
print(flip_bit_to_win(1775))  # Output: 8
print(flip_bit_to_win(7))     # Output: 3
