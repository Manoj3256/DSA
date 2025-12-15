class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit=0
        for i in range(len(nums)):
            bit^=nums[i]
        
        return bit