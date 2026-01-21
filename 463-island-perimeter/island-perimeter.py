class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col,row=len(grid[0]),len(grid)
        p=0
        visited=set()
        def dfs(r,c):
            if r>row-1 or c>col-1 or c<0 or r<0 or grid[r][c]==0:
                return 1
            if (r,c) in visited:
                return 0
            p=0
            visited.add((r,c))
            p+=dfs(r,c+1)
            p+=dfs(r,c-1)
            p+=dfs(r+1,c)
            p+=dfs(r-1,c)
            return p
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    return dfs(i,j)