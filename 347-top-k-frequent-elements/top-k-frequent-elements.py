class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        sort_item = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        result = [item[0] for item in sort_item[:k]]
        return result