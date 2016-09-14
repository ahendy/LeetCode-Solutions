class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        
        def recurse(nums, target, subset, solution, start=0):
            
            if target == 0:
                solution.append(subset)
                
            if target > 0:
                
                for i in range(start, len(nums)): 
                    num = nums[i]
                    if num <= target:
                        recurse(nums, target-num, subset+[num], solution, i)
                    
            
        solution = []
        recurse(candidates, target, [], solution)
        
        return solution 
