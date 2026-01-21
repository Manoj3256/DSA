class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col,row=len(grid[0]),len(grid)
        land=edges=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    land+=1
                    if j+1<col and grid[i][j+1]==1:
                        edges+=1
                    if i+1<row and grid[i+1][j]==1:
                        edges+=1
        return (4*land)-(2*edges)
