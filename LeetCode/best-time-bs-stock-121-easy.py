class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        
        if n < 2:
            return 0
        minval = prices[0]
        result = 0

        for i in range(n):
            result = max(result, prices[i]-minval)
            minval = min(minval, prices[i])
        return result