class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        import heapq as h
        heap=[]
        dic={}
        for i in words:
            dic[i]=dic.get(i,0)+1
        print(dic)
        for key,val in dic.items():
            h.heappush(heap,(-val,key))
        return [h.heappop(heap)[1] for _ in range(k)]