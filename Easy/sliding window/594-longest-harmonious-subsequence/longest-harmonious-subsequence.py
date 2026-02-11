class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        for key in dic.keys():
            if key+1 in dic:
                result=max(result,dic[key]+dic[key+1])
        return result

