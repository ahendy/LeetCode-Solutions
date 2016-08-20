#s API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        half = right = n
        
        while left<right:
            
            half = (left+right)/2
            result = guess(half)

            if result == 1:
                left = half + 1
            
            if result == -1:
                right = half - 1
            
            elif result == 0:
                return half
            
                
        return right 
