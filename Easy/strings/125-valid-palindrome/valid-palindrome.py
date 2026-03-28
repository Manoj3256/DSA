class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result=""
        for c in s:
            if c.isalnum():
                result+=c.lower()
        return result==result[::-1]