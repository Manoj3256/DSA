class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rec(i, curr, best):
            if i == len(nums):
                return best
            curr = max(nums[i], curr + nums[i])
            best = max(best, curr)
            return rec(i+1, curr, best)

        return rec(1, nums[0], nums[0])