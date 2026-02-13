class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        from collections import deque 
        q=deque()
        safe=[]
        length=len(graph)
        revgraph=[[] for _ in range(length)]
        outdegree=[0]*length
        for i in range(length):
            for node in graph[i]:
                outdegree[i]+=1
                revgraph[node].append(i)
        for i in range(length):
            if outdegree[i]==0:
                q.append(i)
        while q:
            top=q.popleft()
            safe.append(top)
            for node in revgraph[top]:
                outdegree[node]-=1
                if outdegree[node]==0:
                    q.append(node)
        return sorted(safe)

        
