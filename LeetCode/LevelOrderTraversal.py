# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        solution = []
        def recurse(root, level):
            
            if root is None:
                return
            
            if level == len(solution):
                solution.append([])
            
            solution[level].append(root.val)    
            recurse(root.left, level+1)
            recurse(root.right, level+1)
            
        recurse(root, 0)
        return solution
            
