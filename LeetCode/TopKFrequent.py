from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        
        c = Counter(nums)
        return [i[0] for i in c.most_common(k)]

