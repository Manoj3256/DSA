class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        import heapq as h
        adj=[[] for _ in range(n)]
        maxpr=[0.0]*n
        maxpr[start_node]=1
        heap=[(-1,start_node)]
        for a,b in enumerate(edges):
            i,j=b
            adj[i].append((j,succProb[a]))
            adj[j].append((i,succProb[a]))
        while heap:
            curr,node=h.heappop(heap)
            curr=-curr
            if node==end_node:
                return curr
            if curr<maxpr[node]:
                continue
            for nextn,nextpr in adj[node]:
                newpr=nextpr*curr
                if newpr>maxpr[nextn]:
                    maxpr[nextn]=newpr
                    h.heappush(heap,(-newpr,nextn))
        return 0.0