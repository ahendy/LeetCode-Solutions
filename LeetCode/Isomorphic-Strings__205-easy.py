class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = {}
        
        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if l.get(a) is None and b not in l.values():
                l[a] = b
            elif l.get(a) != b:
                return False
           
        return True