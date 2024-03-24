# Find the XOR Connects
# You have been given two arrays A,B of sizes n, m respectively. You need to return the total connects in the arrays. A connect is defined as XOR of two elements from different arrays which results in 0.

# Example 1:-

# Input :

# A[ ] = {1,2,3,4,5} ,
# B[ ] = {1,2,3,4,5}

# Output : 5
# Example 2:-

# Input : 
# A[ ]={1,2,3,4,5} ,
# B[ ]={7}

# Output : 0

class Solution:
    def solve(self, a, b):
        count = 0
        i = 0
        j = 0
        a = sorted(a)
        b = sorted(b)
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                i+=1
            elif b[j] < a[i]:
                j+=1
            else:
                count+=1
                i+=1
                j+=1

        return count
    
sol = Solution()
print(sol.solve([1,2,3,4,5], [7]))