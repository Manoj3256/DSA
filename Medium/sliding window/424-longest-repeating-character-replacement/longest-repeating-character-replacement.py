class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        lis=set(s)
        result=0
        for i in lis:
            chance,left=k,0
            for right in range(len(s)):
                if i !=s[right]:
                    chance-=1
                while chance < 0 and left<right:
                    if s[left] != i :
                        chance += 1
                    left += 1
                result=max(result,right-left+1)
        return result