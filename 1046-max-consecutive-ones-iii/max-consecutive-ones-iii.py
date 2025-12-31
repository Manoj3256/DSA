class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=result=zeros=0
        for i in range(len(nums)):
            if nums[i]==0:
                zeros+=1
            while zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
                
            result=max(result,i-left+1)
        return result
