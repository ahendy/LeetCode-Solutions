# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def recurse(l, r):
            if l > r:
                return
            
            mid = (l + r) / 2
            node = TreeNode(nums[mid])
            node.left = recurse(l, mid-1)
            node.right = recurse(mid+1, r)
            
            return node
            
        return recurse(0, len(nums)-1)
