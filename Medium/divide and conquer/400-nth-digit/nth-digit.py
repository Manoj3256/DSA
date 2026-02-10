class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit_length=1
        count=9
        start=1
        while n>digit_length*count:
            n=n-digit_length*count
            count*=10
            digit_length+=1
            start*=10
        num=start+(n-1)//digit_length
        digit=(n-1)%digit_length
        return (int(str(num)[digit]))