class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        s = (sorted((nums)))
        N = len(nums)
        sol = []
        for i in range(0, N-2):
            lo = i+1
            hi = N-1
            
            while lo < hi:
                
                tup = [s[i], s[lo], s[hi]]

                if sum(tup) == 0:
                    sol.append(tup) if tup not in sol else lambda: _
                    hi = hi -1
                
                elif sum(tup) < 0:
                    lo = lo + 1
                    
                else:
                    hi = hi - 1
                    
        return sol
