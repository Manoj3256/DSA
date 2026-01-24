class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def dfs(x,y,visited,graph,w):
            if x==y:
                return w
            visited.add(x)
            for i,val in graph[x]:
                if i not in visited:
                    result=dfs(i,y,visited,graph,val*w)
                    if result!=-1:
                        return result
            return -1  
            
        from collections import defaultdict
        result=[]
        graph=defaultdict(list)
        for (x,y),w in zip(equations,values):
            graph[x].append((y,w))
            graph[y].append((x,1/w))
        for x,y in queries:
            if x not in graph or y not in graph:
                result.append(-1.00)
            elif x==y:
                result.append(1.00)
            else:
                visited=set()
                result.append(dfs(x,y,visited,graph,1.00))
        return result