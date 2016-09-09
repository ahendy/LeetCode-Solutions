# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        
        def recurse(root):
            if root is None: return
            if root and root.left and root.right:
                
                root.left.next = root.right
                
                if root.next:
                    root.right.next = root.next.left
               
            recurse(root.left)
            recurse(root.right)
        
        recurse(root)
            
