class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        dic={}
        result=left=0
        for i in range(len(fruits)):
            dic[fruits[i]]=dic.get(fruits[i],0)+1

            while len(dic)>2:
                dic[fruits[left]]-=1
                if dic[fruits[left]]==0:
                    del dic[fruits[left]]
                left+=1
            result=max(result,i-left+1)
        return result
