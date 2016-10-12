# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def recurse(root, isleft=False):
            if root is None:
                return 0
            
            if isleft and not root.left and not root.right:
                val = root.val
            else:
                val = 0
                
            return val + recurse(root.left, True) + recurse(root.right, False)
            
        return recurse(root)
            
