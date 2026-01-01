class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def rec(lis,k,s,result):
            if lis==[]:
                return result
            curr,chance,left=lis[0],k,0
            for right in range(len(s)):
                if curr!=s[right]:
                    chance-=1
                while chance < 0:
                    if s[left] != curr:
                        chance += 1
                    left += 1

                result=max(result,right-left+1)
            return rec(lis[1:],k,s,result)
        lis=list(set(s))
        return rec(lis,k,s,0)