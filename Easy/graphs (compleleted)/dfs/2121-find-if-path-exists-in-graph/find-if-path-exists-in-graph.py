class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        g=[[]for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        visited=[False]*n
        def dfs(root):
            if root==destination:
                return True
            visited[root]=True
            for i in g[root]:
                if not visited[i]:
                    if dfs(i):
                        return True
            return False
        return dfs(source)
