class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        swapos = 0
        
        for i in xrange(len(nums)):
            num = nums[i]
            if num != 0:
                nums[swapos] = num
                swapos += 1
                
        
        for i in xrange(swapos, len(nums)):
            nums[i] = 0
