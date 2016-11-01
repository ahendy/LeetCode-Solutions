class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def recurse(nums, i, sol):
            if i == len(nums)-1:
                sol.append(nums)
                
            for j in range(i, len(nums)):
                if j != i and nums[i] == nums[j]: continue
                nums = list(nums)
                nums[i], nums[j] = nums[j], nums[i]
                recurse(nums, i+1, sol)
                
                
        sol = []
        nums.sort()
        recurse(nums, 0, sol)
        return sol
