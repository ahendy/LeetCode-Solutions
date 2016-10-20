class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sp = fp = 0
        while sp < len(s) and fp < len(t):
            sp += s[sp] == t[fp]
            fp += 1
        
        return sp == len(s)
