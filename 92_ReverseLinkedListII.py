# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        if not head:
            return None
        
        # Create a dummy node to simplify reversing the first part of the list
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move prev to the node just before the left-th node
        for i in range(left - 1):
            prev = prev.next

        # Initialize current and next pointers
        current = prev.next
        next_node = None

        # Reverse the sublist from left to right
        for i in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next

        
