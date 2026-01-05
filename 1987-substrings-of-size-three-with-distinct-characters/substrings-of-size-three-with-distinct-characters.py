class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic,count,left={},0,0
        for right in range(len(s)):
            dic[s[right]]=dic.get(s[right],0)+1
            if right-left+1==3:
                if len(dic)==3:
                    count+=1
                    print(count)
                if dic[s[left]]>1:
                    dic[s[left]]=dic.get(s[left],0)-1
                else:
                    del dic[s[left]]
                left+=1
        return count