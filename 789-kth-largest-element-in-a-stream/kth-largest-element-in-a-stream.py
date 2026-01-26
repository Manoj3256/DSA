class KthLargest(object):

    import heapq
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k
        self.heap=[]
        for x in nums:
            self.add(x)
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
        elif val>self.heap[0]:
            heapq.heappush(self.heap, val)
            heapq.heappop(self.heap)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)