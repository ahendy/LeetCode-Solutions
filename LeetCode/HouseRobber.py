class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums)<=2:
            return max(nums)
            
        dp = [0]*len(nums)
        
        dp[0], dp[1]  = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
            
        """Recursive Soln"""    
        # index = 0
        # def recurse(nums, dp, i):
        #     if i >= len(nums):
        #         return 0
            
        #     dp[~i] = max(recurse(nums, dp, i+1), nums[~i] + recurse(nums, dp, i+2))
        #     return dp[~i]

        # recurse(nums, dp, 0)
        return dp[-1]
        
        
        
