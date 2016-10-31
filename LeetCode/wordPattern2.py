class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        if len(pattern) != len(str) or not pattern or not str:
            return False
            
        memo = {}
        z = zip(pattern, str)
        f = lambda k, v: k in memo and v != memo[k]
        
        for k, v in z:
            if f(k, v) or (k not in memo and v in memo.values()):
                return False
            else:
                memo[k] = v
                
        return True
