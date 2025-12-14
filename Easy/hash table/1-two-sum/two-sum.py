class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}   

        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in seen:
                return [seen[rem], i]

            seen[nums[i]] = i
