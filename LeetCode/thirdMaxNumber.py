class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        window = [None] * 3
        
        for num in nums:
            min_of_max = window[0]
            if num not in window and num > min_of_max:
                # pop then push new val
                heapq.heappushpop(window, num)
        
        
        return window[0] if window[0] is not None else max(window)
            
        
