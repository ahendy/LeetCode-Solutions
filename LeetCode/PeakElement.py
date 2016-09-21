class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return False
        
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (-lo+hi)/2
            
            if nums[mid] < nums[mid+1]:
                lo = mid+1
            else:
                hi = mid
            
        return hi
