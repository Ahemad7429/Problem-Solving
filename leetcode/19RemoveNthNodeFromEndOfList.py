# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    # Dummy node to handle edge cases
    dummy = ListNode(0)
    dummy.next = head
    
    # Find the length of the linked list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    # Find the node before the nth node from the end
    prev = dummy
    for _ in range(length - n):
        prev = prev.next
    
    # Remove the nth node from the end
    prev.next = prev.next.next
    
    return dummy.next
