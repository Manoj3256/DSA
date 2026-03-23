class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result=0
        for i in columnTitle:
            result=result*26+(ord(i)-ord("A")+1)
        return result