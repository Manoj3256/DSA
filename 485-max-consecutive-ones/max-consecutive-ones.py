class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=length=0
        for right in range(len(nums)):
            if nums[right]==1:
                length+=1
            else:
                length=0
            result=max(length,result)
        return result