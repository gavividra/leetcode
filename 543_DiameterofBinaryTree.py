# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        '''
        counter = 0
        if root.left:
            counter += 1
            counter += diameterOfBinaryTree(self, root.left)
        if root.right:
            counter += 1
            counter += diameterOfBinaryTree(self, root.right)
        return counter
        '''

        '''
        answer = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            answer = max(answer, left + right)
            return 1 + max(right, left)
        depth(root)
        return answer
        '''
    'Solution'
        self.diameter=0
        self.height(root,self.diameter)
        return self.diameter
    
    def height(self,root,diameter):
        if root is None:
            return 0
        lh=self.height(root.left,self.diameter)
        rh=self.height(root.right,self.diameter)
        self.diameter=max(self.diameter,lh+rh)
        return 1+max(lh,rh)
