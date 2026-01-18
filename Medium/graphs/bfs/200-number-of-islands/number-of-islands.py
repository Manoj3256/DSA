class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        from collections import deque
        if not grid: return 0
        R,C,ans =len(grid),len(grid[0]),  0
        for r in range(R):
            for c in range(C):
                if grid[r][c]=="1":
                    ans+=1
                    q=deque([(r,c)])
                    grid[ r][c]="0"
                    while q:
                        x,y=q.popleft()
                        for dx ,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            nx,ny =x+dx,y+dy
                            if 0<=nx<R and 0<=ny<C and grid[nx][ny]=="1":
                                grid[nx][ny]="0"
                                q.append((nx,ny))
        return ans

