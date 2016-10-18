# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        def recurse(root, path):
            print path
            if not root:
                return False 
            path += root.val
            if not root.left and not root.right:
                return path == sum
                
            return recurse(root.left, path) or recurse(root.right, path)
        
        return recurse(root, 0)
