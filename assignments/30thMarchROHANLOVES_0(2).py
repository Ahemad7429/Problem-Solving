# ROHAN LOVES 0 (2)
# Rohan loves 0, he has been assigned a task by his coach to find all the indexes of an array having length n, such that on those indexes say i, 0<=i<=n-1, the absolute difference between PrefixSum[i] and SuffixSum[i] is 0.

# Note: Prefix Sum : Prefix Sum[i] is defined as the sum of all the values of the array up to index i.

# PrefixSum[0]=nums[0];

# PrefixSum[1]=nums[0]+nums[1];

# PrefixSum[i]=nums[0]+nums[1]+nums[2]+........nums[i].

# Suffix Sum : Suffix Sum[i] is defined as the sum of all the values from end of the array up to index i.

# Suffix Sum[n-1] = nums[n-1];

# Suffix Sum[n-2] = nums[n-2]+nums[n-1];

# Suffix Sum[i] = nums[i]+nums[i+1]+nums[i+2]+........nums[n-1].

# Constraints:

# 1<=n<=10^4;

# -10^4<=nums[i]<=10^4;

# Sample test cases:

# Input:
# {4, 2, -3, 1, 6}

# Output:
# {1};

# `Input:
# {1, 2, -2, 3}

# `Output: {1 2};

def find_zero_diff_indices(nums):
    n = len(nums)
    
    # Compute prefix sum array
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]
    
    # Compute suffix sum array
    suffix_sum = [0] * n
    suffix_sum[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + nums[i]
    
    # Find indices where absolute difference between prefix sum and suffix sum is 0
    zero_diff_indices = []
    for i in range(n):
        if prefix_sum[i] == suffix_sum[i]:
            zero_diff_indices.append(i)
    
    return zero_diff_indices

# Test cases
print(find_zero_diff_indices([4, 2, -3, 1, 6]))  # Output: [1]
print(find_zero_diff_indices([1, 2, -2, 3]))     # Output: [1, 2]

