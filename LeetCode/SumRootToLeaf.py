# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def recurse(root, s):
            
            if not root:
                return 0
            
            s = 10*s + root.val
            if not root.left and not root.right:
                return s
            
            return recurse(root.left, s) + recurse(root.right, s)
            
        return recurse(root, 0)
        
            
