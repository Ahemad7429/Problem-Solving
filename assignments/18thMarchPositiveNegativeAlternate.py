
# Positive Negative Alternate
# In a town, residents have a unique way of arranging numbers in arrays. They prefer to maintain an alternating pattern of positive and negative numbers to create a harmonious sequence. However, sometimes they need a little help rearranging their arrays to achieve this pattern.

# Task:

# As an assistant to the townspeople of Alternville, your task is to write a function that takes an array of integers as input and rearranges it to create an alternating pattern of positive and negative numbers. If there are more of one kind than other (meaning if there are more positive numbers or more negative numbers) you should move all the remaining to the end of the array and **if there is a zero do not include it in the array**.  
#  Also make sure that positive and negative numbers are sorted in their own individual group, for example, if the given array is  [-1, 3,4,-6,2,5,9,-2] then the output should be: [-1,2,-2,3,-6,4,5,9].
# The resulting array should start with the lowest number of the given array.
# Input:

# An integer n (1 ≤ n ≤ 100), represents the number of elements in the array.
# A list of n integers, where each integer is in the range of -1000 to 1000 (inclusive).
# Output:

# A list of n integers, representing the rearranged array with an alternating positive-negative pattern.

# Sample Input:

# 8
# -5,-2,3,4,-1,9,-7,-10
# Sample Output:

# -1,3,-2,4,-5,9,-7,-10


class Solution:

    def alternatePandE(self, ar):
            i = 0
            j = 0
            if len(ar) > 1:
                j = 1

            while i < j:
                while ar[i] <= 0:
                    i+=2
                while ar[j] > 0:
                    j+=2
                if i < j:
                    ar[i], ar[j] = ar[j], ar[i] 
            print(ar)


sol = Solution()
sol.alternatePandE([-5,-2,3,4,-1,9,-7,-10])