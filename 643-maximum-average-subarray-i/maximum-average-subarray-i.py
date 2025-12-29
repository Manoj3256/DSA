class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left=wsum=0
        result=-5000
        for i in range(len(nums)):
            wsum+=nums[i]
            if i-left+1>= k:
                result=max(result,float(wsum)/k)
                wsum-=nums[left]
                left+=1
        return result