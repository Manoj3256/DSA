class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent=[x for x in range(len(edges)+1)]
        def find(x):
            if parent[x]!=x:
                return find(parent[x])
            return parent[x]
        def union(x,y):
            fx,fy=find(x),find(y)
            if fx==fy:
                return False
            parent[fy]=fx
            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]
