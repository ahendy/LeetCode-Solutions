class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums)-1
        while i != 0 and nums[i] <= nums[i-1]:
            i -= 1
        
        if i == 0:
            nums[:] = reversed(nums)
       
        else:
            j = len(nums)-1
            while nums[j] <= nums[i-1]:
                j -= 1
            
            nums[j], nums[i-1] = nums[i-1], nums[j]
            nums[i:] = list(reversed(nums[i:]))
