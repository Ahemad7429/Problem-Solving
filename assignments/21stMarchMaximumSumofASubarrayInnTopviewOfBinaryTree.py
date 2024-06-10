# Maximum Sum of a Subarray in Topview of Binary Tree
# Given a binary tree, find the maximum sum of a subarray in its top view. The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

# A subarray in the top view is defined as the sum of values of nodes visible from the top at any specific horizontal distance.

# Input:

# The function takes a pointer to the root of the binary tree root (1 <= nodes <= 10^4).
# Output:

# Return an integer representing the maximum sum of a subarray in the top view.

# Example:

# Input:
#       1
#      /\
#     2   3
#    / \  / \
#   4   5 6   7
# [1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1]

# Output:
# 17

# Explanation:
# The top view is [4, 2, 1, 3, 7], and the maximum sum subarray is [4, 2, 1, 3, 7] with a sum of 17.

# Note:

# Nodes of the binary tree have values in the range [-1000, 1000].
# The binary tree will not be empty.
# Ensure that your solution has a time complexity of O(N), where N is the number of nodes in the binary tree.


from collections import deque, defaultdict

class Solution:
  def top_view(self, root):
      if not root:
          return []
      
      queue = deque([(root, 0)])
      top_view_map = {}
      
      while queue:
          node, hd = queue.popleft()
          
          if hd not in top_view_map:
              top_view_map[hd] = node.val
          
          if node.left:
              queue.append((node.left, hd - 1))
          if node.right:
              queue.append((node.right, hd + 1))
      
      min_hd = min(top_view_map.keys())
      max_hd = max(top_view_map.keys())
      
      top_view_nodes = [top_view_map[hd] for hd in range(min_hd, max_hd + 1)]
      
      return top_view_nodes
  
  def max_sum_subarray(self, arr):
      max_sum = float('-inf')
      current_sum = 0
      
      for num in arr:
          current_sum += num
          if current_sum > max_sum:
              max_sum = current_sum
          if current_sum < 0:
              current_sum = 0
      
      return max_sum
  
  def maxSumTopView(self, root):
      top_view_nodes = self.top_view(root)
      return self.max_sum_subarray(top_view_nodes)

