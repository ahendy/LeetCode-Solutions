class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 1
            
        n_i = [0, 1]
        
        for i in range(2, n+1):
            n_i.append(n_i[i-1]+n_i[i-2])
        
        return n_i[-1] + n_i[-2]
