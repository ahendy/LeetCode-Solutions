class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        # candidates =  filter(lambda x: x <= target, candidates)
        candidates = sorted(candidates)
        def recurse(nums, target, subset, solution, start=0):
            
            if target == 0 and subset not in solution: solution.append(subset)
                
            if target > 0:
                i = start
                while i < len(nums):
                    
                    num = nums[i]
                    if num<=target:
                        recurse(nums, target-num, subset+[num], solution, i+1)
            
                    i = i+1
            
        solution = []
        recurse(candidates, target, [], solution)
        
        return solution
