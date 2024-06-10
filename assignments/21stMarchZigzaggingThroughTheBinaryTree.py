# Zigzagging through the Binary Tree
# At HeyCoach, a dedicated mentor is determined to assist students with their problems. The students are organized in a tree-like fashion, with each student representing a node in a binary tree. The mentor can offer support to a student by personally visiting them, but there's a catch - he can only move in a zigzag pattern! This means that after helping a student, the mentor must choose the next student from the opposite direction. He can either move to the left child and then to the right child, or vice versa.

# The mentor aims to maximize the number of students he can provide support to during his zigzag traversal. Your task is to help the mentor by finding out the maximum number of students he can assist at HeyCoach.

# Example 1
# Input
# root = [3,9,20,N, N,15,7]

#       3
#      / \
#     9   20
#        / \
#       15  7
            
# Output:

# 3
# Explanation :

# Ram is travelling in the path:- 3->20->15 20 is the right child of 3 15 is the left child of 20

# Thus, the total nodes travelled: 3

# Example 2:
# Input:
# root = []
# Output:

# 0
# Example 3:
# Input:
# root = [5 4 8 11 N 13 4 7 2 N N 5 1]
# Output:
# 3
# Constraints:
# The number of nodes in the tree is in the range [0, 200000].

# -1000 <= Node.val <= 1000

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.max_zigzag_length = 0

        def dfs(node, direction, length):
            if not node:
                return
            self.max_zigzag_length = max(self.max_zigzag_length, length)
            if direction == "left":
                if node.left:
                    dfs(node.left, "right", length + 1)
                if node.right:
                    dfs(node.right, "left", 1)
            elif direction == "right":
                if node.right:
                    dfs(node.right, "left", length + 1)
                if node.left:
                    dfs(node.left, "right", 1)

        if root.left:
            dfs(root.left, "right", 1)
        if root.right:
            dfs(root.right, "left", 1)

        return self.max_zigzag_length

# Example usage:
# Construct the tree: [3,9,20,None,None,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.longestZigZag(root))  # Output: 3
