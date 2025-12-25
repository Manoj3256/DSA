class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        listed=set(nums2)
        res=[]
        for i in range(len(nums1)):
            if nums1[i] in listed:
                listed.remove(nums1[i]) 
                res.append(nums1[i])

        return res