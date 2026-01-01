class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        lis=set(s)
        chance,result=k,0
        for i in lis:
            chance=k
            left=0
            for right in range(len(s)):
                if i !=s[right]:
                    chance-=1
                while chance < 0 and left<right:
                    if s[left] != i :
                        chance += 1
                    left += 1
                result=max(result,right-left+1)
        return result
        # def rec(lis,k,s,result):
        #     if not lis:
        #         return result
        #     curr,chance,left=next(iter(lis)), k,0
        #     for right in range(len(s)):
        #         if curr!=s[right]:
                    
        #             chance-=1
        #         while chance < 0:
        #             if s[left] != curr:
        #                 chance += 1
        #             left += 1

        #         result=max(result,right-left+1)
        #     lis.remove(curr)
        #     return rec(lis,k,s,result)
        # lis=set(s)
        # return rec(lis,k,s,0)