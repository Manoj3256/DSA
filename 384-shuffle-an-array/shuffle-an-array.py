import random

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original=self.current =nums[:]
          
        
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.current =self.original[:] 
        return self.current
        
    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffle = self.original[:] 
        for i in range(len(shuffle)-1, 0, -1):
            j = random.randint(0, i)
            
            shuffle[i], shuffle[j] = shuffle[j], shuffle[i]
            
        self.current = shuffle  
        return self.current