ass Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s)
        s = list(s)
        
         # return self.reverseStringRecurse(s, 0, len(s)-1)
         # return self.reverseString2(s)
         # return self.reverseString3(s)
        
        for i in range(n/2):
            s[i], s[~i] = s[~i], s[i]
        
        return "".join(s)
            
    def reverseString2(self, s):
        return s[::-1] # makes a new string
    
    def reverseString3(self, s):
        return "".join(reversed(list(s))) # preserves s
        
    def reverseStringRecurse(self, s, lo=0,hi=None):
        if hi<=lo:
            return "".join(s)
        
        s[lo],s[hi] = s[hi], s[lo]
        return self.reverseStringRecurse(s, lo+1, hi-1)
        
        
        
