class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        row,col=len(heights),len(heights[0])
        pacific=set()
        atlantic=set()
        def dfs(r,c,visited,value):
            if r<0 or c<0 or c>col-1 or r>row-1 or (r,c) in visited or heights[r][c]<value:
                return
            visited.add((r,c))
            dfs(r-1,c,visited,heights[r][c]) 
            dfs(r+1,c,visited,heights[r][c]) 
            dfs(r,c+1,visited,heights[r][c]) 
            dfs(r,c-1 ,visited ,heights[r][c])

        for i in range(row):
            dfs(i,0,pacific,heights[i][0])
            dfs(i,col-1,atlantic,heights[i][col-1])
        for j in range(col):
            dfs(0,j,pacific,heights[0][j])
            dfs(row-1,j,atlantic,heights[row-1][j])
        return list (pacific&atlantic)