class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph=[[]for _ in range(n)]
        for i,j in dislikes:
            graph[i-1].append(j-1)
            graph[j-1].append(i-1)
        color=[-1]*n
        for i in range(n):
            if color[i]==-1:
                color[i]=0
                q=deque([i])
                while q:
                    a=q.popleft()
                    for b in graph[a]:
                        if color[b]==-1:
                            color[b]=1-color[a]
                            q.append(b)
                        elif color[a]==color[b]:
                            return False
        return True