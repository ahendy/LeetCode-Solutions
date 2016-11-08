class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        memo = collections.defaultdict(list)
        for s in strs:
            memo[tuple(sorted(s))].append(s)
        
        return memo.values()
            
