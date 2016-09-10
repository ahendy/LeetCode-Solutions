class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return  0
            
        if len(nums)<= 2:
            return max(nums)
            
        def robit(nums):
            
            now = prev = 0
            for num in nums:
                now, prev = max(now, num + prev), now
                
            return now
            
            
        return max(robit(nums[1:]), robit(nums[:-1]))
            
