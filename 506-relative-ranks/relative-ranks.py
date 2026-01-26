class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        import heapq
        rank=1
        heap=[]
        result=[""]*len(score)
        for i in range(len(score)):
            heapq.heappush(heap,(-score[i],i))
        while heap:
            _,pos=heapq.heappop(heap)
            if rank==1:
                result[pos]="Gold Medal"
            elif rank==2:
                result[pos]="Silver Medal"
            elif rank==3:
                result[pos]="Bronze Medal"
            else:
                result[pos]=str(rank)
            rank+=1
        return result