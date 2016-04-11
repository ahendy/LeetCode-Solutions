# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    _highestdepth = 0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxRecurse(root, 0)
        return self._highestdepth
        
    def maxRecurse(self, root, depth):
        if root is None:
            return
        depth = depth+1
        self.maxRecurse(root.left, depth)
        self.maxRecurse(root.right, depth)
        
        if depth>self._highestdepth:
            self._highestdepth = depth
            
            
        