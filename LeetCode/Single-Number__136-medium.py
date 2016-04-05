class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        foundsum, expectedsum = 0, 0
        seen = {}
        
        for i in nums:
            if seen.get(i) is None:
                expectedsum += 2 * i
                seen[i] = 1
            foundsum += i
            
        
            
        return expectedsum - foundsum # results in difference of expected sum        
    