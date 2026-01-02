class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic={}
        for i,n in enumerate(nums):
            if n in dic and i-dic[n]<=k:
                return True
            dic[n]=i
            
        return False