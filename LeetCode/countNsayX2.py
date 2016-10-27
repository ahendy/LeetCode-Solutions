class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        curr = '1'
        
        for i in range(1, n):
            count = 1
            next = ""
            for j in range(len(curr)):
                if j == len(curr)-1 or curr[j] != curr[j+1]:
                    next += str(count) + curr[j]
                    count = 1
                
                else:
                    count += 1
                    
            curr = next
    
        return curr
                
