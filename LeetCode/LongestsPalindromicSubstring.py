class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        
        l = ''.join(['#', '#'.join(s), '#'])

        
        maxx = 1
        curlo, curhi = 0, 1

        for i in xrange(len(l)):
            
            x = 1
            lo = i-x
            hi = i+x
            
            while  i-x >=0 and i+x < len(l) and l[lo] == l[hi]:

                if x > maxx:
                    curlo = i-x
                    curhi = i+x
                    maxx = x
                
                x += 1
                lo = i-x
                hi = i+x
                
          
        return l[curlo+1:curhi+1:2]
