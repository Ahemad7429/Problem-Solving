# Most Frequent Element
# You have been given an array of elements. You need to return the most frequent element. In case of more than 1 element having the same highest frequency. Return the frequency of the smallest of those.

# Sample Input:

# 9

# 5 5 5 6 6 6 7 7 8

# Sample Output:

# 5

# Constraints-

# 1 <= arr.size <= 1e5

# 1 <= arr[i] <= 1e9

class Solution:
    def MostFrequent(self, arr):
        frequency = {}

        for ele in arr:
            if ele in frequency:
                frequency[ele] += 1
            else:
                frequency[ele] = 1
        
        max_frequency = max(frequency.values())
        most_frequent_elements = [key for key, value in frequency.items() if value == max_frequency]
        return min(most_frequent_elements)