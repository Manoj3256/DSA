class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def stairs(n,cache):
            
            if n<=0:
                return 1
            if cache[n] is not None:
                return cache[n]
            else:
                if n>1:
                    cache[n]=stairs(n-2,cache)+stairs(n-1,cache)
                else:
                    cache[n]=stairs(n-1,cache)
            return cache[n]
        cache=[None]*( n+1)
        return stairs(n,cache)
