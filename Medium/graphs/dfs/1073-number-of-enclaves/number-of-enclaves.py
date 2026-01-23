class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row,col=len(grid),len(grid[0])
        visited=set()
        def dfs(r,c,visited):
            if r<1 or c<1 or r>row-2 or c>col-2 or (r,c) in visited or grid[r][c]==0:
                return 
            visited.add((r,c))
            grid[r][c]=0
            dfs(r+1,c,visited)
            dfs(r-1,c,visited)
            dfs(r,c+1,visited)
            dfs(r,c-1,visited)
        for i in range(row):
            for j in range(col):
                if grid[0][j]==1:
                    grid[0][j]=0
                    dfs(1,j,visited)
                if grid[row-1][j]==1:
                    grid[row-1][j]=0
                    dfs(row-2,j,visited)
                if grid[i][0]==1:
                    grid[i][0]=0
                    dfs(i,1,visited)
                if grid[i][col-1]==1:
                    grid[i][col-1]=0
                    dfs(i,col-2,visited)
        return sum( grid[i][j] for i in range(row) for j in range(col))