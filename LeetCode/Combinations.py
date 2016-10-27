class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        nums = range(1, n+1)
        print nums
        def recurse(nums, i, path, sol):
            if len(path) == k:
                sol.append(path)
                return
            
            if len(path) + len(nums) - i < k:
                return
        
            recurse(nums, i+1, path+[nums[i]], sol)
            recurse(nums, i+1, path, sol)
        
        sol = []
        recurse(nums, 0, [], sol)
        return sol
