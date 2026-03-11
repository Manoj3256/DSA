class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        l=len(image[0])
        result=[[0]*l for _ in range(l)]
        print(result)
        for i in range(l):
            for j in range(l):
                result[i][j]=1-image[i][(l-1)-j]
        return result