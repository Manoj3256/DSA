class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        maxlen= left = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left] )
                left += 1

            seen.add(s[i])
            maxlen=max(maxlen, i - left + 1)
        
        return maxlen
