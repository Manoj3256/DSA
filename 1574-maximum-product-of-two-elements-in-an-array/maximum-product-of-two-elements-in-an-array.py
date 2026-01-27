class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq as h
        heap=[]
        for i in nums:
            h.heappush(heap,i)
            if len(heap)>2:
                h.heappop(heap)
        return ((h.heappop(heap)-1)*(h.heappop(heap)-1))