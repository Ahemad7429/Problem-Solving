# First Negative element in evry window size k
# In the town of Kanpur, where technology intertwined with everyday life, lived a young programmer named Nitin. One sunny afternoon, while strolling through the local park, she stumbled upon an antique book filled with intricate coding riddles.
# Determined to crack the enigma, Nitin found a puzzling task: to locate the first negative integer within every subarray of window size k in a given sequence(say arr) of size N . Help Nitin in solving this task.

# Example:

# Input:

# k= 3
# arr={12, -1, -7, 8, -15, 30, 16, 28}  
# Output:

# -1 -1 -7 -15 -15 0 
# Constraints:

# 1 <= N <= 10^5
# 10^5 <= A[i] <= 10^5
# 1 <= K <= N

def first_negative_in_window(arr, n, k):
    # Initialize the result list and list to store indices of negative numbers
    result = []
    neg_indices = []

    # Process the first window of size k
    for i in range(k):
        if arr[i] < 0:
            neg_indices.append(i)

    # For the rest of the windows
    for i in range(k, n):
        # If there are any negative numbers in the current window
        if neg_indices:
            result.append(arr[neg_indices[0]])
        else:
            result.append(0)
        
        # Remove the elements which are out of this window
        while neg_indices and neg_indices[0] <= i - k:
            neg_indices.pop(0)
        
        # Add the current element if it is negative
        if arr[i] < 0:
            neg_indices.append(i)

    # For the last window
    if neg_indices:
        result.append(arr[neg_indices[0]])
    else:
        result.append(0)

    return result

# Test the function with an example input
k = 3
arr = [12, -1, -7, 8, -15, 30, 16, 28]
n = len(arr)
print(first_negative_in_window(arr, n, k))  # Output: [-1, -1, -7, -15, -15, 0]