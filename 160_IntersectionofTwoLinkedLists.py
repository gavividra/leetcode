# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #Given Wierd Solution
        a = headA
        b = headB
        while a != b:
            if a:
                a=a.next
            else:
                a=headB
            if b:
                b=b.next
            else:
                b=headA
        return a

        '''
        # Confused by return value -- Version 1
        intersectVal = 0
        change = False
        listA = []
        listB = []
        skipA = 0
        skipB = 0
        while headA:
            listA.append(headA)
            headA = headA.next
        while headB:
            listB.append(headB)
            if headB.val in listA and change == False:
                intersectVal = headB.val
                change = True  
            headB = headB.next
        while headA:
            skipA += 1
            if headA.val == intersectVal:
                break
            headA = headA.next
        while headB:
            skipB += 1
            if headB.val == intersectVal:
                break
            headB = headB.next
        return "Intersected at '%d'" % (intersectVal)
        '''
        
        
