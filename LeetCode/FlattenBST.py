# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def recurse(root):
            if not root:
                return
            
            recurse(root.left)
            recurse(root.right)
            
            if root.left:
                r = root.right
                root.right = root.left
                left = root.left
                while left.right:
                    left = left.right
                
                left.right = r
                root.left = None
        
        recurse(root)
                
            