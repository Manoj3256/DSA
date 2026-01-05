class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic,count,left={},0,0
        for right in range(len(s)):
            dic[s[right]]=dic.get(s[right],0)+1
            print("added",dic)
            if right-left+1==3:
                print("entered to 3 window")
                if len(dic)==3:
                    count+=1
                    print(count)
                if dic[s[left]]>1:
                    dic[s[left]]=dic.get(s[left],0)-1
                    print("deleted",s[left])
                else:
                    print("deleted",s[left])
                    del dic[s[left]]
                left+=1
        return count