class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import deque
        target=len(graph)-1
        res=[]
        q=deque()
        q.append([0])
        while q:
            path=q.popleft()
            node=path[-1]
            if node==target:
                res.append(path)
                continue
            for nei in graph[node]:
                q.append(path + [nei])
        return res
