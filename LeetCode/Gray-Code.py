class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        sol = [0]
        for i in range(n):
            sol += [x + (1<<i) for x in reversed(sol)]
        
        return sol
