from collections import defaultdict
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
            if d[num] == 3:
                del d[num]
        
        return d.keys()[0]
