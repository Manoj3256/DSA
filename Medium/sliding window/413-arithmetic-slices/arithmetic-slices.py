class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        resultcount=0
        left=0
        rec=result=0
        def recursion(rec_length,resultcount):
            for right in range(len(nums)-rec_length+1):
                left=right+1
                rec=nums[left]-nums[right]
                while left<len(nums):
                    if nums[left]-nums[left-1]==rec:
                        if left-right+1==rec_length:
                            resultcount+=1
                    else:
                        break
                    left+=1
            return resultcount
        for i in range(3,len(nums)+1):
            result+=recursion(i,resultcount)
        return result