class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        friends=range(1,n+1)
        def game(friends,k,i):
            if len(friends)==1:
                return friends[0]
            i=(i+k-1)%len(friends)
            del friends[i]
            return game(friends,k,i)
        return game(friends,k,0)
