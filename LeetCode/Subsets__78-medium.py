class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        sol = []
        for i in range(2**n):
            b = (bin(i))[:1:-1]
            appendlist = []
            for l in range( len(b) ):
                if b[l] == '1':
                    appendlist.append( nums[l] )
            sol.append(appendlist)
        
        
        return sol