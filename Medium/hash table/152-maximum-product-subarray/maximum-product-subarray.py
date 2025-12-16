class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_pro = min_pro = res= nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_pro, min_pro = min_pro, max_pro


            max_pro = max(nums[i], max_pro * nums[i])
            min_pro = min(nums[i], min_pro * nums[i])

            res = max(res, max_pro)

        return res
