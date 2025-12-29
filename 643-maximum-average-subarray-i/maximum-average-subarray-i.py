class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left=0
        wsum=sum(nums[0:k])
        result=float(wsum)/k
        for i in range(k,len(nums)):
            wsum+=nums[i]
            wsum-=nums[left]
            left+=1
            result=max(result,float(wsum)/k)
        return result