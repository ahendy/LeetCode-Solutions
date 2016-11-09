class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        s = []
        
        for d in num:
            while k > 0 and s and s[-1] > d:
                s.pop()
                k -= 1
            
            s.append(d)
        
        k *= -1
        if not k:
            k = None
        
        return "".join(s[:k]).lstrip('0') or '0'
