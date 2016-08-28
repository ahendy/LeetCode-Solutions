# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        sol = []
        def recurse(root):
            if root is None:
                return
            
            recurse(root.left)
            sol.append(root.val)
            recurse(root.right)
            
        recurse(root)
        return sol
