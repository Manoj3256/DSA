class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        length=len(s)
        for i in range(length//2):
            if s[i]!=s[length-i-1]:
                s[i]=s[length-i-1]=min(s[i],s[length-i-1])
        return "".join(s)
