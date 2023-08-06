# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        'Version 1'
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
        
        'Version 2'
        temp = head
        counter = 1
        while head.next:
            head = head.next
            counter += 1
            if counter % 2 == 0:
                temp = temp.next
        return temp
