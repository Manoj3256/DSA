class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import deque
        graph=[[] for _ in range(numCourses)]
        indegree,visited=[0]*numCourses,0
        q=deque()
        for i,j in prerequisites:
            indegree[i]+=1
            graph[j].append(i)
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            value=q.pop()
            visited+=1
            for i,j in prerequisites:
                if j==value:
                    indegree[i]-=1
                    if indegree[i]==0:
                        q.append(i)
        return visited==numCourses