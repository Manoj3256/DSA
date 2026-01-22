class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        keys=[False]*len(rooms)
        def dfs(rooms,visited,i):
            print(visited,i)
            visited[i]=True
            for j in rooms[i]:
                if not visited[j]:
                    dfs(rooms,visited,j)
        dfs(rooms,keys,0)
        if False in keys:
            return False
        else:
            return True









        # for i in range(1,len(rooms)):
        #     print("keys",keys)
        #     if i in keys:
        #         keys.extend(rooms[i])
        #     else:
        #         return False
        # return True
