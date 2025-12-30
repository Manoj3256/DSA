class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if len(nums)<k or k==1:
            return 0
        result=float('inf')
        left=0
        nums.sort()
        while left+k-1<len(nums):
            if nums[left+k-1]-nums[left]<result:
                result=nums[left+k-1]-nums[left]
            
            print(nums[left+k-1],nums[left],nums[left+k-1]-nums[left])
            left+=1
        return result