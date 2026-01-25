class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n==1:
            return [0]
        elif n ==2:
            return [0, 1]
        from collections import deque
        q=deque()
        indegree,tree=[0]*n,[[]for _ in range(n)]
        for i,j in edges:
            tree[i].append(j)
            tree[j].append(i)
            indegree[i]+=1
            indegree[j]+=1
        for i in range(n):
            if indegree[i] ==1:
                q.append(i)
        while n>2:
            n-=len(q)
            for _ in range(len(q)):
                last_nodes=q.popleft()
                for i in tree[last_nodes]:
                    indegree[i]-=1
                    if indegree[i]==1:
                        q.append(i)
        return list(q)
