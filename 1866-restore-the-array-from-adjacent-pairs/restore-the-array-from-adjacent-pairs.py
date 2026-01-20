class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        res=[]
        visited=set()
        graph=defaultdict(list)
        for i,j in adjacentPairs:
            graph[i].append(j)
            graph[j].append(i)
        for node in graph:
            if len(graph[node] )==1:
                starting=node
                break
        def dfs(node):
            visited.add(node)
            res.append(node)
            for a in graph[node]:
                if a not in visited:
                    dfs(a)
        dfs(starting)
        return res
