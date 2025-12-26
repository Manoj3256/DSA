class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dic={}
        for i in range(len(nums)):
            if nums[i]in self.dic:
                self.dic[nums[i]].append(i)
            else:
                self.dic[nums[i]]=[i]
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random as r
        l=len(self.dic[target])
        j=r.randint(0,l-1)
        return self.dic[target][j]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)