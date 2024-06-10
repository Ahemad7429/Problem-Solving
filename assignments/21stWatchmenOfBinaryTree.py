# Watchmen of Binary Tree
# Given HeyCoach land’s Binary Tree Society, we have to place watchmen to keep an eye on the whole Society, each watchman can keep an eye on itself, parent node and immediate children. Calculate minimum number of Watchmen required to keep an eye on all houses of the HeyCoach Land.

# For example: Given the Binary Tree

#        1
#      /   \
#    2       3
#   /    
#  6
# The minimum number of watchmen would be two which can be placed at node value '2' and '3'.

# Input Format:

# A single line that represents the value of the nodes and the value of '- 1' denotes NULL node.
# Output Format:

# Return a single integer representing the minimum number of watchmen required to keep an eye on the society.
# Sample Input:

# 1 2 3 6 -1 -1 -1 -1 -1

# Sample Output:

# 2
# Constraints:

# 0 <= N <= 10^4

# 0 <= data <= 10^3

# Where 'N' denotes the total number of nodes and 'data' denotes the value of the node

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.watchmen_count = 0

    def minWatchmen(self, root):
        def dfs(node):
            if not node:
                return 1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left == 0 or right == 0:
                self.watchmen_count += 1
                return 2
            
            if left == 2 or right == 2:
                return 1
            
            return 0
        
        if dfs(root) == 0:
            self.watchmen_count += 1
        
        return self.watchmen_count

# Helper function to build a binary tree from a list of values
def build_tree(values):
    if not values or values[0] == -1:
        return None
    
    root = Node(values[0])
    queue = [root]
    index = 1
    
    while index < len(values):
        node = queue.pop(0)
        
        # Left child
        if index < len(values) and values[index] != -1:
            node.left = Node(values[index])
            queue.append(node.left)
        index += 1
        
        # Right child
        if index < len(values) and values[index] != -1:
            node.right = Node(values[index])
            queue.append(node.right)
        index += 1
    
    return root

# Example usage
values = [1, 2, 3, 6, -1, -1, -1, -1, -1]
root = build_tree(values)
solution = Solution()
print(solution.minWatchmen(root))  # Output: 2

# Additional example:
values = [1, 2, -1, 3, 4, -1, -1, 5, -1, -1, -1]
root = build_tree(values)
print(solution.minWatchmen(root))  # Output: 2
