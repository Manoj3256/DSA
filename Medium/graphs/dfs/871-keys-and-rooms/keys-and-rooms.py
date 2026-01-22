class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        keys=[False]*len(rooms)
        def dfs(rooms,visited,i):
            visited[i]=True
            for j in rooms[i]:
                if not visited[j]:
                    dfs(rooms,visited,j)
        dfs(rooms,keys,0)
        if False in keys:
            return False
        else:
            return True