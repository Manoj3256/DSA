class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        (a,b),(c,d)=edges[0],edges[1]
        if a==c or a==d:
            return a
        return b