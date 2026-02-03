class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        def majority(nums,i,n,dic):
            if i>=n:
                return max(dic.items())[0]
            if nums[i] in dic:
                dic[nums[i]]=dic.get(nums[i],0)+1
                if dic[nums[i]]>(n/2):
                    return nums[i]
            else:
                dic[nums[i]]=1
            return majority(nums,i+1,n,dic)
        return majority(nums,0,len(nums),dic)