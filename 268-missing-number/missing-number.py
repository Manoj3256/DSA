class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=min(nums)
        l=max(nums)
        for i in range(l+1):
            if i not in nums:
                return i
        return l+1
