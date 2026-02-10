class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        from collections import deque
        leng=len(graph)
        print(leng)
        color=[-1]*leng
        for i in range(leng):
            if color[i]==-1:
                color[i]=0
                q=deque([i])
                while q:
                    u=q.popleft()
                    for a in graph[u]:
                        if color[a]==-1:
                            color[a]=1 if color[u]==0 else 0
                            q.append(a)
                        elif color[a]==color[u]:
                            return  False
        return True
