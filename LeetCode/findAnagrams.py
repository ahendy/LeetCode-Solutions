from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pc = Counter(p)
        n = len(p)
        sol = []
        
        if len(s) < n:
            return []
        
        window_count = Counter()
        for i in range(n-1):
            window_count[s[i]] += 1
            
        for i in range(len(s)-n+1):
            first, nxt  = s[i], s[i+n-1]
            
            window_count[nxt] += 1
            
            if pc == window_count:
                sol.append(i)
                
            window_count[first] -= 1
            if window_count[first] == 0:
                del window_count[first]
            

        return sol
            
            
        
        
