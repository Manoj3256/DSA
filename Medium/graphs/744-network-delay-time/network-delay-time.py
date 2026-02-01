class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        #dijkstra's algorithm
        import heapq as h
        mintime=[float('inf')]*n
        mintime[k-1]=0
        q=[(0,k-1)]
        adj=[[] for _ in range(n)]
        for i,j,t in times:
            adj[i-1].append([j-1,t])
        while q:
            curr,node=h.heappop(q)
            if curr>mintime[node]:
                continue
            for nextn,nextt in adj[node]:
                newtime=nextt+curr
                if newtime<mintime[nextn]:
                    mintime[nextn]=newtime
                    h.heappush(q,(newtime,nextn))
        a=max(mintime)
        return a if a!=float('inf') else -1