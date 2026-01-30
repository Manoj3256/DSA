class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        import heapq
        lis=[int(x) for x in str(num)]
        odd,even,res=[],[],[]
        for i in lis:
            if i%2==0:
                heapq.heappush(even, -i)
            else:
                heapq.heappush(odd, -i)
        for i in lis:
            if i%2==0:
                res.append(-heapq.heappop(even))
            else:
                res.append(-heapq.heappop(odd))
        return int("".join( map(str, res)))
