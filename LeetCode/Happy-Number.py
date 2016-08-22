class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        mem = set()
        
        def recurser(n, mem):
            if n==1:
                return True
                
            n = list(str(n))
            new = sum(map(lambda x: int(x)**2, n))
            
            if new in mem:
                return False
            
            n = int("".join(str(new)))
            
            return recurser(n, mem | {new})
        
        return recurser(n, mem)
