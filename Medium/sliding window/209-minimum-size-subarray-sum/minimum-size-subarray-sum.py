class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        result,temp,left=float('inf'),0,0
        for right in range(len(nums)):
            temp+=nums[right]
            while temp>=target:
                if result>(right-left+1):
                    result=(right-left+1)
                temp-=nums[left]
                left+=1


        return 0 if result==float('inf') else result