class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = min(len(nums)-1, k-1)
        h = [-n for n in nums]
        heapq.heapify(h)
        
        
        for j in xrange(k):
            heapq.heappop(h)
            
        
        return -heapq.heappop(h)
        
        
