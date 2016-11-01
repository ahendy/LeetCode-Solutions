class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def recurse(nums, i, sol):
            if i == len(nums)-1:
                sol.append(nums)
                
            for j in range(i, len(nums)):
                nums = list(nums)
                nums[i], nums[j] = nums[j], nums[i]
                recurse(nums, i+1, sol)
                
                
        sol = []
        recurse(nums, 0, sol)
        return sol
                
                
