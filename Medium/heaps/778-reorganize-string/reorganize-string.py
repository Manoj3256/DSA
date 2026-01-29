class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic,result={},[]
        prevcount,prevval=0,''
        heap=[]
        for i in s:
            dic[i]=dic.get(i,0)+1
            if dic[i]>(len(s)+1)//2:
                return ""
        for val,count in dic.items():
            heapq.heappush(heap,(-count,val))
        while heap:
            count,val=heapq.heappop(heap)
            result.append(val)
            if prevcount<0:
                heapq.heappush(heap,(prevcount,prevval))
            prevval,prevcount=val,count+1
        return "".join(result)

