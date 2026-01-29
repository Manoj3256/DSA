class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        import heapq as h
        heap=[]
        for val in stones:
            h.heappush(heap,(-val))
        while len(heap)>1:
            val1=h.heappop(heap)
            val2=h.heappop(heap)
            if val1!=val2:
                h.heappush(heap,val1-val2)
        return -heap[0] if len(heap)==1 else 0

