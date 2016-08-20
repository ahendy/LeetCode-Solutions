#tion for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
       
        
        def recurse(left, right):
            
            if left == None or right == None:
                return left==right
                
            if left.val!=right.val:
                return False
            
            return all( (recurse(left.left, right.right), recurse(left.right, right.left)))
        
        return root==None or recurse(root.left, root.right)
            
