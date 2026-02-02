class Solution(object):
    def isPalindrome(self, n):
        """
        :type x: int
        :rtype: bool
        """
        if n<0:
            return False
        num=n
        rev=0
        while n!=0:
            rev=rev*10+n%10
            n//=10
        return num==rev