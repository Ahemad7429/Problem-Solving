# Sweepers Problem
# You are managing a team of sweepers responsible for cleaning a series of roads in a city. Each road has a certain length, represented by an array of integers. Given the lengths of these roads and the number of sweepers available, your goal is to assign the sweepers to the roads in a continuous manner to minimize the total time required for cleaning all the roads.

# Input Format:

# The first line contains an integer, N, representing the number of roads.
# The second line contains Nspace-separated integers, each representing the length of thei-th road.
# The third line contains an integer, K, representing the number of sweepers.
# Output Format:

# Print a single integer representing the minimum time required to clean all the roads.
# Constraints:

# 1 <= N <= 105
# 1 <= Length of each road (A[i]) <= 10^6
# 1 <= K <= N
# Sample Input:

# 5
# 5 10 30 20 15
# 3
# Sample Output:

# 35
# Explanation:

# Given 5 roads with lengths [5, 10, 30, 20, 15]and 3 sweepers, the optimal way to distribute the workload among the sweepers ensures that all roads are cleaned in a minimum total time of35. This output implies that the work distribution strategy must result in the least possible maximum work done by any sweeper, considering the sweepers work on continuous sections of roads.


def is_valid_distribution(roads, max_time, sweepers):
    current_sum = 0
    sweeper_count = 1
    
    for length in roads:
        if current_sum + length > max_time:
            sweeper_count += 1
            current_sum = length
            if sweeper_count > sweepers:
                return False
        else:
            current_sum += length
            
    return True

def minimum_time_to_clean(roads, sweepers):
    left, right = max(roads), sum(roads)
    result = right
    
    while left <= right:
        mid = (left + right) // 2
        if is_valid_distribution(roads, mid, sweepers):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result

# Reading input
N = int(input())
roads = list(map(int, input().split()))
K = int(input())

# Calculate the minimum time required to clean all roads
print(minimum_time_to_clean(roads, K))
