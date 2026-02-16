class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        graph=[[]for _ in range(n)]
        for i,j in redEdges:
            graph[i].append([j,0])
        for i,j in blueEdges:
            graph[i].append([j,1])
        result=[-1]*n
        q=deque([(0,0,-1)])
        visited=[]
        while q:
            val,dis,col=q.popleft()
            if result[val]==-1:
                result[val]=dis
            for nextnode,color in graph[val]:
                if color!= col and (nextnode,color) not in visited:
                    visited.append((nextnode,color))
                    q.append((nextnode,dis+1,color))    
        return result


