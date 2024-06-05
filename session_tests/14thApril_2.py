# Rotate lists
# Given the head of a linked list, rotate the list to the right by k places.

# Input:
# head: The head of the linked list. (0 <= length of the list <= 500)
# k: The number of places to rotate the list. (0 <= k <= 2 * 10^9)

# Output:
# Return the head of the rotated linked list.

# Examples:

# Input:

# head = [1,2,3,4,5], k = 2

# Output:
# [4,5,1,2,3]
# Input:

# head = [0,1,2], k = 4

# Output:

# [2,0,1]

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100

# class Solution:
#     def rotateRight(self, head, k): 
#       if not head:
#           return None
      
#       length = 1
#       tail = head
      
#       while tail.next:
#           tail = tail.next
#           length += 1
      
#       k = k % length
      
#       if k == 0:
#           return head
      
#       new_tail = head
#       for _ in range(length - k - 1):
#           new_tail = new_tail.next
      
#       new_head = new_tail.next
#       new_tail.next = None
#       tail.next = head
#       return new_head