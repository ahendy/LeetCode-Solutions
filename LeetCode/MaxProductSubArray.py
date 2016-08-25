class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxsofar = b = s = nums[0]
        numsd = list(nums)
        for i in range(1, len(nums)):
            a =  (nums[i], nums[i]*b, nums[i]*s)
            b = max(a)
            s = min(a)
            maxsofar = max(b, maxsofar)
            
        
        return maxsofar
        
                
            

