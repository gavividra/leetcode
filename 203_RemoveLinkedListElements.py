# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        beginning = ListNode(0)
        beginning.next = head
        temp = beginning
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next 
        return beginning.next
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
