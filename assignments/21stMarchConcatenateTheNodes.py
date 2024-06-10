# Concatenate the Nodes
# Given a Binary Tree of N Nodes having integer values . Your Task is to find out the Largest Number that could be formed by concatenating all its nodes values.

# For example:
# Given the Binary Tree

#        5
#      /    \
#   34       47
#  /    
# 6
# The answer would be 654734 since by concatenating the node values this is the highest number possible.

# Input Format:
# A single line that represents the value of the nodes and the value of '- 1' denotes NULL node.
# Output Format:
# Print the integer that represents the largest number that could be formed by concatenating all its nodes given in a Binary Tree.
# Sample Input:
# 5 34 47 6 -1 -1 -1 -1 -1

# Sample Output:
# 654734
# Constraints:
# 0 <= N <= 10^4

# 0 <= data <= 10^3

# Where 'N' denotes the total number of nodes and 'data' denotes the value of the node.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def concatenate(self, root):
        if not root:
            return ""
        
        # Perform BFS to collect all node values
        def bfs_collect(root):
            queue = [root]
            node_values = []
            while queue:
                node = queue.pop(0)
                node_values.append(str(node.data))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return node_values
        
        node_values = bfs_collect(root)
        
        # Custom sorting based on concatenation
        node_values.sort(key=lambda x: x*10, reverse=True)
        
        # Join sorted values to form the largest number
        return ''.join(node_values)

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
values = [5, 34, 47, 6, -1, -1, -1, -1, -1]
root = build_tree(values)
solution = Solution()
print(solution.concatenate(root))  # Output: "654734"

# Additional example:
values = [1, 2, 3, -1, -1, -1, -1]
root = build_tree(values)
print(solution.concatenate(root))  # Output: "321"
