class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        right,index,seen=0,[],[]
        dic={}
        for i in p:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        left,need=0,len(p)
        for right in range(len(s)):
            if s[right] in dic:
                if dic[s[right]] >0:
                    need-=1
                dic[s[right]]-=1

            if right-left+1> len(p):
                if s[left] in dic:
                    if dic[s[left]]>= 0:
                        need+=1
                    dic[s[ left]]+=1
                left+=1
            if need ==0:
                index.append(left)


        return index