class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in t:
            if i in dic:
                if dic[i]>0:
                    dic[i]-=1
                else:
                    return False
            else:
                return False
        return True