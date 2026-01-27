class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq as h
        heap=[]
        for i,x in enumerate(nums):
            h.heappush(heap,(x,i))
            if len(heap)>k:
                h.heappop(heap)
        heap.sort(key=lambda x: x[1]) 
        return [i for i,_ in heap]