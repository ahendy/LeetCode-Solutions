# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        order = []
        def recurse(root):
            if root is None:
                return
            
            order.append(root.val)
            recurse(root.left)
            recurse(root.right)
        
        recurse(root)
        return order
