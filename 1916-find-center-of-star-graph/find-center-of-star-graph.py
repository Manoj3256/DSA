class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        maxval = 0
        for u,v in edges:
            maxval=max(maxval, u, v)
        g = [[]for _ in range(maxval + 1)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        for i in range(1,len(g)):
            if len(g[i])==len(edges):
                return i