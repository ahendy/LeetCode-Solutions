class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
            
        count = 0
        # grid = map(list, grid)
        N, m = range(len(grid)), range(len(grid[0]))
        
        def dfs(i, j):
            if i not in N or j not in m or grid[i][j] != '1' : 
                return
            
            grid[i][j] = 'x' # void current spot
            dfs(i+1, j) # Dfs suurrounding pixels only if value is also a 1
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for i in N:
            for j in m:
                if grid[i][j] == '1': 
                    # found an island
                    count += 1
                    dfs(i, j) # dfs from i,j to fill in rest of island
        return count