class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #SQRT(X) is the value where sqrt(x)*sqrt(x) = x
        
        lo, hi = 0, x
        mid = hi

        
        while lo < hi:
            mid = (hi+lo)/2
            
            if mid*mid < x < (mid+1)*(mid+1):
                return mid
            
            elif mid*mid < x:
                lo = mid+1
            
            else:
                hi = mid

        
        return lo
