class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if self.revr(x,0) == x:
            return True
        return False
        
    
    def revr(self, x, r=0):
        
        while x!=0:
            r = 10*r + x%10
            x = x/10
            
        return r
        
        