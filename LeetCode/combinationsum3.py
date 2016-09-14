class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        solution = []
        def recurse(k, n, subset, solution, start):
            
            if k==0 and n==0:
                solution.append(subset)
            if k==0:
                return
            
            i = start
            while i < 10:
                recurse(k-1, n-i, subset+[i], solution, i+1) 
                
                i = i + 1
                
        recurse(k, n, [], solution, 1)
        return solution
