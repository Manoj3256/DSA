class Solution(object):
    def floodFill(self, image, sr, sc, color):
        t=image[sr][sc]
        if t==color:
            return image
        self.dff(image,sr,sc,color,t)
        return image
    def dff(self,image,sr,sc,color,t):
        
        roe=len(image[0])
        l1=len(image)
        if sr < 0 or sr >= l1 or sc < 0 or sc >= roe:
            return

        elif image[sr][sc]!=t:
            return
        image[sr][sc]=color
        self.dff(image,sr+1,sc,color,t)
        self.dff(image,sr,sc+1,color,t)
        self.dff(image,sr-1,sc,color,t)
        self.dff(image,sr,sc-1,color,t)
    
        
        
