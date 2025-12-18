class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo={}
        def rec(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]

            memo[i]= max(nums[i] + rec(i+2), rec(i+1))
            return memo[i]
        
        return rec(0)