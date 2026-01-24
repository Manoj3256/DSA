class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph,res=[[] for _ in range(numCourses)],[]
        indegree=[0]*numCourses
        q=deque()
        for i,j in prerequisites:
            graph[j].append(i)
            indegree[i]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            value=q.popleft()
            res.append(value)
            for i in graph[value]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        return res if len(res)==numCourses else []

