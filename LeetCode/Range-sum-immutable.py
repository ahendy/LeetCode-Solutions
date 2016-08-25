class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        listsum = [0]
        for i in nums:
            listsum += [listsum[-1] + i]
        self.listsum = listsum
        
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        sol = 0
        top = self.listsum[j+1]
        bot = self.listsum[i]
        sol = top-bot
        return sol