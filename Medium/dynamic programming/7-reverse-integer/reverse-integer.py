class Solution(object):
    def reverse(self, num):
        """
        :type x: int
        :rtype: int
        """
        max=(2**31)-1
        min=2**31
        sign=-1 if num<0 else 1

        n=abs(num)
        rev=0
        while n!=0:
            digit=n%10
            if rev>(max-digit)//10:
                return 0
            rev=rev*10+n%10
            n//=10
        return sign*rev
