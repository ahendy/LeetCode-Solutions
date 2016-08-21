class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """       
        lmap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        setlist = [lmap[d] for d in digits]
        solution = []
        
        if not digits:
            return solution
            
        def recurse(setlist, index, sol, l):
            
            if index == len(setlist):
                sol += ["".join(l)]
                return
           
            head =  setlist[index]
            for ch in head:
                 curr = (recurse(setlist, index+1, sol, l +[ch]))
                          
            return
            
        recurse(setlist, 0, solution, [])
        
        return solution
            
            
