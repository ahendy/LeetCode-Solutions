from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        c = Counter(s)
        # Old
        # return len(s) - (sum((x % 2 for x in c.itervalues() if x % 2))) + int(any(x%2 for x in c.itervalues()))
        
        # New 
        # i&~1 is the closest even digit less than or equal to i
        return sum(i&~1 for i in c.itervalues()) + int(any(x%2 for x in c.itervalues()))
        
            
