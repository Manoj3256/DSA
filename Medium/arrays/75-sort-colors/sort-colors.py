class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        s,i = 0,0             
        l = len(nums) - 1   

        while i <= l:
            if nums[i] == 0:
                nums[s], nums[i] = nums[i], nums[s]
                s += 1
                i += 1

            elif nums[i] == 1:
                i += 1

            else:  
                nums[l], nums[i] = nums[i], nums[l]
                l -= 1


        return nums 