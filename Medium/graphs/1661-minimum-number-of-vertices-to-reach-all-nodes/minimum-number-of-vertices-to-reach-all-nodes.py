class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        result=[]
        indegree=[0]*(n)
        for _,j in edges:
            indegree[j]+=1
        for i in range(n):
            if indegree[i]==0:
                result.append(i)
        return (result)
