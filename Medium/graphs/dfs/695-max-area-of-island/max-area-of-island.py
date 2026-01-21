class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col,row=len(grid[0]),len(grid)
        large=area=0
        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=col or grid[r][c]==0:
                return 0
            grid[r][c]=0
            area=1
            area+=dfs(r+1,c)
            area+=dfs(r-1,c)
            area+=dfs(r,c+1)
            area+=dfs(r,c-1)
            return area
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    large=max(large,dfs(i,j))
        return large
