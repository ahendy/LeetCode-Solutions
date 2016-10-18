class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def pall(s):
            return s == s[::-1]
            
        def next_partition(s, curr, res):
            if not s:
                res.append(curr)
            
            for i in range(1, len(s)+1):
                if pall(s[:i]):
                    next_partition(s[i:], curr + [s[:i]], res)
                    
        
        res = []
        next_partition(s, [], res)
        
        return res
