class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        dic,left,need={},0,len(s1)
        for i in s1:
            dic[i]=dic.get(i,0)+1
        for right in range(len(s2)):
            if s2[right] in dic:
                if dic[s2[right]]>0:
                    need-=1
                dic[s2[right]]-=1
            if right-left+1>len(s1):
                if s2[left] in dic:
                    if dic[s2[left]]>=0:
                        need+=1
                    dic[s2[left]]+=1
                left+=1

            if need==0:
                return True
        return False

