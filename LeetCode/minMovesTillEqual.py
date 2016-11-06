class Solution(object):
    def minMoves(self, nums):

        if not nums:
            return 0
            
        m = min(nums)
        count = 0
    
        for num in nums:
            count += num - m
            
        return count
