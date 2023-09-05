"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        node_mapping = {}

        temp = head
        while temp:
            new_node = Node(temp.val)
            node_mapping[temp] = new_node
            temp = temp.next
        
        temp = head
        while temp:
            if temp.random:
                node_mapping[temp].random = node_mapping[temp.random]
            if temp.next:
                node_mapping[temp].next = node_mapping[temp.next]
            temp = temp.next
        
        return node_mapping[head]
        

            
