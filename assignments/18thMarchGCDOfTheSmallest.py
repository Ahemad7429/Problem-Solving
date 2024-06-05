class Solution:
    def gcd(self, a, b):
        # Base case: If b is 0, then the GCD is a
        if b == 0:
            return a
        # Recursive case: Compute GCD of b and remainder of a divided by b
        return self.gcd(b, a % b)
    
    def solve(self, ar):
         # Sort the array in non-decreasing order
        ar.sort()
        
        total_cost = 0
        while len(ar) > 1:
            # Calculate the cost (GCD) of the current operation
            operation_cost = self.gcd(ar[0], ar[1])
            total_cost += operation_cost
            
            # Append the result of the operation back to the array
            ar.append(ar[0] + ar[1])
            
            # Remove the two smallest numbers from the array
            ar = ar[2:]
            
            # Re-sort the array after appending the result
            ar.sort()
        
        return total_cost

# Test the function
n = 5
ar = [5, 4, 2, 3, 1]
print("Output:", Solution().solve(ar))
