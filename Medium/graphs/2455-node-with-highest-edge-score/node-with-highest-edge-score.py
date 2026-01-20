class Solution(object):
    def edgeScore(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        l=[0]*len(edges)
        large=float('-inf')
        for i in range(len(edges)):
            l[edges[i]]+=i
            if large<l[edges[i]]:
                large=l[edges[i]]
        return l.index(large)