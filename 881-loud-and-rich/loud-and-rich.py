class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        def dfs(i,graph,result):
            if result[i]!=float('inf'):
                return result[i]
            result[i]=i
            for ele in graph[i]:
                person=dfs(ele,graph,result)
                if quiet[person]<quiet[result[i]]:
                    result[i]=person
            return result[i]

        n=len(quiet)
        graph=[[]for _ in range(n)]
        #creating adj graph
        for i,j in richer:
            graph[j].append(i)
        result=[float('inf')]*n
#function call
        for i in range(n):
            dfs(i,graph,result)
        return result
