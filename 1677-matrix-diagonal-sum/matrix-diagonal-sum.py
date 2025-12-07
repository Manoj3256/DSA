class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        s=0
        for i in range(0,len(mat)):
            s+=mat[i][i]+mat[i][len(mat)-i-1]
        if(len(mat)%2==1):
            n=len(mat)//2
            s-=mat[n][n]
            
        return s