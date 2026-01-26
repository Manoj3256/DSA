class MedianFinder(object):

    def __init__(self):
        import heapq
        self.max=[]
        self.min=[]
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if  not self.max or num<=-self.max[0]:
            heapq.heappush(self.max,-num)
        else:
            heapq.heappush(self.min,num)
        if len(self.min)>len(self.max):
            heapq.heappush(self.max,-heapq.heappop(self.min))
        elif len(self.max)>len(self.min)+1:
            heapq.heappush(self.min,-heapq.heappop(self.max))
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min)==len(self.max):
            return (self.min[0]+(-self.max[0]))/2.0
        elif len(self.max)>len(self.min):
            return -self.max[0]
        else:
            return self.min[0]
    

    # def findMedian(self):
    #     if len(self.max) == len(self.min):
    #         return (-self.max[0] + self.min[0]) / 2.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()