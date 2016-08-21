from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ws = longest = 0
        d = defaultdict(int).fromkeys(string.printable)
        
        for i, ch in enumerate(s):
            if d[ch] >= ws:
                ws = d[ch] + 1
            
            d[ch] = i
            longest = max(longest, i-ws+1)
            
        return longest
        
        
