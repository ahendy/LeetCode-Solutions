class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x,y: 26*x + y, map(lambda x: ord(x) - ord('A') +1, s))
