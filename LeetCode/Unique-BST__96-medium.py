import math
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = math.factorial(2 * n)
        b = math.factorial(n + 1)
        c = math.factorial(n)
        return a / (b * c)
                