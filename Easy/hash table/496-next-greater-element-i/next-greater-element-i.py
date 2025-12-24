class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic,t,res={},0,[]
        for i in range(len(nums2)-1):
            count=i
            while count<len(nums2):
                if nums2[i]<nums2[count]:
                    dic[nums2[i]]=nums2[count]
                    break
                count+=1
        for i in nums1:
            if i in dic:
                t=dic[i]
                res.append(t)
            else:
                res.append(-1)
        return res