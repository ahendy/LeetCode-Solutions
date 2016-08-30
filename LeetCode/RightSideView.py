# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        sol = []
        def recurse(root, sol, depth=0):
            
            if root is None:
                return
            if depth == len(sol): # each depth has one right side
            # so will contain a new rightmost (since right recurses first)
                sol.append(root.val)
            recurse(root.right, sol, depth+1)
            recurse(root.left, sol, depth+1)
        
        recurse(root, sol)
        return sol
