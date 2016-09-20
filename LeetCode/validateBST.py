# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root, least=-9999999999,most=9999999999):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
            
        if root.val <= least or root.val >= most:
            return False
            
        
        return self.isValidBST(root.left, least, root.val) and \
               self.isValidBST(root.right, root.val, most)
        
