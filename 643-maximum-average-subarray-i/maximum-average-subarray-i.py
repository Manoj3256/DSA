class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if 1==len(nums):
            return float(nums[0])
        left=wsum=0
        result=float('-inf')
        for i in range(len(nums)):
            wsum+=nums[i]
            if i-left+1>= k:
                result=max(result,float(wsum)/k)
                wsum-=nums[left]
                left+=1
        return result