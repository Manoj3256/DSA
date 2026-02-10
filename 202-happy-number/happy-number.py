class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic={}
        while n!=1:
            if n in dic:
                return False
            else:
                dic[n]=1
            sum=(n%10)**2
            while n>0:
                n/=10
                sum+=(n%10)**2
            n=sum
        return True 