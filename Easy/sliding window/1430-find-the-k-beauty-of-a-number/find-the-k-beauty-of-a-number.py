class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        string=str(num)
        count=0
        for left in range(len(string)-k+1):
            temp=int(string[left:left+k])
            if temp!=0 and num%temp==0:
                count+=1
        return count