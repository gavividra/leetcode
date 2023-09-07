# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # Step 1: Calculate the length of the linked list
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        # Step 2: Calculate the size of each part and the remainder
        part_size = length // k
        remainder = length % k

        # Step 3: Split the linked list into k parts
        result = []
        temp = head

        for i in range(k):
            part_head = temp
            part_length = part_size + (1 if i < remainder else 0)

            if part_head:
                # Find the tail of the current part
                for j in range(part_length - 1):
                    temp = temp.next

                # Save the next node and disconnect the current part
                Next = temp.next
                temp.next = None
                result.append(part_head)

                # Move to the next part
                temp = Next
            else:
                # If there are no more nodes, append None
                result.append(None)

        return result
