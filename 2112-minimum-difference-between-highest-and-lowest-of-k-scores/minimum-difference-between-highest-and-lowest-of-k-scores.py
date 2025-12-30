class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if len(nums)<k:
            print("less length")
            return 0
        result=float('inf')
        left=0
        num=sorted(nums)
        print(num)
        while left+k-1<len(num):
            if num[left+k-1]-num[left]<result:
                result=num[left+k-1]-num[left]
            
            print(num[left+k-1],num[left],num[left+k-1]-num[left])
            left+=1
        return result