class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p = pattern
        s = str.split()
        return len(s) == len(p) and len(set(p)) == len(set(s)) == len(set(zip(s,p)))
