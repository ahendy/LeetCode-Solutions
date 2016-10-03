class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def reversal(x):
            v = 0
            
            while x != 0:
                r = x % 10
                v = 10*v + r
                x /= 10
            
            return v if v < (2**31) -1 else 0
        
        return [1, -1][x < 0] * reversal(abs(x))
