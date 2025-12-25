class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic,res={},[]
        for i in nums2:
            if i not in dic:
                dic[i]=1
                
        for i in nums1:
            if i in dic:
                dic.pop(i) 
                res.append(i)
        return res