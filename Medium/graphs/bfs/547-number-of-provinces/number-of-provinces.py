class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        from collections import  deque
        n,result=len(isConnected),0
        visited=set( )
        for i in range(n):
            if i not in visited:
                q=deque([i])
                visited.add(i)
                while q:
                    item=q.popleft()
                    for j in range(n):
                        if isConnected[item][j]==1 and j not in visited:
                            visited.add(j)
                            q.append(j)
                result+=1
        return result

        
