class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result=[[1]for _ in range(numRows)]
        def pascal(result,num,i):
            if i>num:
                return result            
            length=len(result[i-1])
            if length==i:
                return pascal(result,num,i+1)
            if length<i-1:
                result[i-1].append(result[i-2][length-1]+result[i-2][length])
            if length==i-1:
                result[i-1].append(1)
            return pascal(result,num,i)
        return pascal(result,numRows,1)
        