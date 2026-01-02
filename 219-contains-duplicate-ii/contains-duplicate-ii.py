class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        left,insidewin=0,set()
        for right in range(len(nums)):
            if nums[right] in insidewin:
                return True
            insidewin.add(nums[right])
            if right-left ==k:
                insidewin.remove(nums[left])
                left+=1
        return False