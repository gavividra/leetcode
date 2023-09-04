# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        # Version 1
        if not head:
            return False
        curr = head
        while curr:
            print("curr: " + str(curr.val))
            if curr.next and curr.next == curr:
                return True
            temp = head
            while temp and temp != curr:
                print("temp: " + str(temp.val))
                if curr.next == temp:
                    return True
                temp = temp.next
            curr = curr.next
        return False
        '''

        # Version 2
        if not head or not head.next:
            return False
    
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
        
