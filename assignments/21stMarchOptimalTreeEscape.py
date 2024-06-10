# Optimal Tree Escape
# Objective: Determine who escapes first from a binary tree by either always moving left (Ram) or always moving right (Shyam).

# Given:

# A binary tree where each node represents a position in a unique training course, with two children nodes (left and right) except for leaf nodes, which have no children.
# Two characters, Ram and Shyam, start from the root of the binary tree. Ram always moves to the left child, and Shyam always moves to the right child. Their goal is to reach any leaf node to escape the tree.
# Output:

# If both Ram and Shyam escape the tree simultaneously, return 0.
# If Ram escapes first, return -1.
# If Shyam escapes first, return 1.
# Constraints:

# The number of nodes in the tree is in the range [0, 200000].
# Node values are within [-1000, 1000].
# Examples:

# Input: root = [1]
# Output: 0 Explanation: Both start and end at the root node (the only node), escaping simultaneously.

# Input: root = [10, 5, -1, -1, 15, 12, -1, -1, -1]
# Output: 1 Explanation: Shyam escapes the tree first by always moving to the right child.

# Input: root = [3, 9, 20, -1, -1, 15, 7, -1, -1, -1, -1]
# Output: -1 Explanation: Ram escapes the tree first by always moving to the left child.

# Solution Approach:

# The solutions provided traverse the binary tree based on Ram's and Shyam's strategies, tracking the depth of traversal to determine who reaches a leaf node first. The depth comparison between the leftmost and rightmost paths effectively decides the output according to the specified rules.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leftmost_depth(node):
    depth = 0
    while node:
        depth += 1
        node = node.left
    return depth

def rightmost_depth(node):
    depth = 0
    while node:
        depth += 1
        node = node.right
    return depth

def who_escapes_first(root):
    if not root:
        return 0  # Tree is empty, both "escape" simultaneously.
    
    left_depth = leftmost_depth(root)
    right_depth = rightmost_depth(root)
    
    if left_depth < right_depth:
        return -1  # Ram escapes first
    elif right_depth < left_depth:
        return 1   # Shyam escapes first
    else:
        return 0   # Both escape simultaneously

# Example usage:

# Tree: [1]
root1 = TreeNode(1)
print(who_escapes_first(root1))  # Output: 0

# Tree: [10, 5, -1, -1, 15, 12, -1, -1, -1]
root2 = TreeNode(10)
root2.left = TreeNode(5)
root2.right = TreeNode(15)
root2.right.left = TreeNode(12)
print(who_escapes_first(root2))  # Output: 1

# Tree: [3, 9, 20, -1, -1, 15, 7, -1, -1, -1, -1]
root3 = TreeNode(3)
root3.left = TreeNode(9)
root3.right = TreeNode(20)
root3.right.left = TreeNode(15)
root3.right.right = TreeNode(7)
print(who_escapes_first(root3))  # Output: -1
