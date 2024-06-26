# Special Arrangements
# You're a daring jewel thief infiltrating the vault of the century, protected by a complex combination lock. Each dial holds a glittering gem, their values encoded in integers (represented by the nums array).
# To crack the lock, you need to arrange the gems in a specific order: for each adjacent pair, either the first gem's value must divide evenly into the second's, or vice versa. But cracking such a combination requires more than just brute force!

# You're given an array of nums containing the values of the vault's gems (n distinct positive integers between 1 and 10^9).
# Your mission is to find the total number of possible "special" arrangements of these gems, where every pair satisfies the divisibility requirement (i.e., forms a harmonious sequence). Since the number of special arrangements can be huge, you need to return the answer modulo 10^9 + 7 to avoid numerical overflows.

# Input/Output Format:
# Input:
# An array nums containing the gem values separated by spaces or commas.

# Output:
# Return a single integer representing the total number of special gem arrangements modulo 10^9 + 7.

# Examples:
# Input:
# 2 3 6 (Three gems in the vault)

# Output:
# 2 (Only two arrangements work: [3 6 2] and [2 6 3])

# Input:
# 1 4 3 (Another vault to plunder)

# Output:
# 2 (Similar to the first example, only two special arrangements exist: [3 1 4] and [4 1 3])

# Constraints:
# 2 <= n <= 14 (Number of gems in the vault)
# 1 <= nums[i] <= 10^9 (Individual gem value)


class Solution:
    def is_special(self, arrangement):
      for i in range(1, len(arrangement)):
          if arrangement[i] % arrangement[i-1] != 0 and arrangement[i-1] % arrangement[i] != 0:
              return False
      return True

    def generate_permutations(self, nums, permutation, visited, special_count):
        if len(permutation) == len(nums):
            if self.is_special(permutation):
                special_count[0] += 1
            return
        
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                permutation.append(nums[i])
                self.generate_permutations(nums, permutation, visited, special_count)
                permutation.pop()
                visited[i] = False
              
    def special_arr(self, nums):
        MOD = 10**9 + 7
        special_count = [0]
        
        self.generate_permutations(nums, [], [False] * len(nums), special_count)
        
        return special_count[0] % MOD