# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, goal):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        def recurse(root, sum, path, sol):
            if root is None:
                return 
            
            sum += root.val
            if not root.left and not root.right:
                # leaf
                if sum == goal:
                    sol.append(path + [root.val])
                    return 
                else:
                    return
                
            recurse(root.left, sum, path + [root.val], sol)
            recurse(root.right, sum, path + [root.val], sol)                    
                    
        sol = []            
        recurse(root, 0, [], sol)
        
        return sol
                    
                 
