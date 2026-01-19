class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if len(trust)<n-1:
            return -1
        first=[0]*(n+1)
        secp=[0]*(n+1)  
        for i,j in trust:
            first[j]+=1
            secp[i]+=1
        for i in range(1,n+1):
            if first[i]==n-1 and secp[i]==0:
                return i
        return -1
