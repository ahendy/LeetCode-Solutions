class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        lo, hi = 0, len(nums)-1
        
        while lo < hi:
            sum = nums[lo] + nums[hi]
            if sum > target:
                hi = hi - 1
            elif sum < target:
                lo = lo + 1
            else:
                return lo+1, hi+1
        
        return -1,-1
