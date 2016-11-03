class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        profitsofar = 0
        minsofar = maxsofar = prices[0]
        
        for price in prices:
            
            if price < minsofar:
                maxsofar = minsofar = price

            else:
                maxsofar = max(price, maxsofar)
            
            profitsofar = max(profitsofar, maxsofar-minsofar)
    
        return profitsofar
