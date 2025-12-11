class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        ans=[""]*len(words)
        for w in words:
            p=int(w[-1])
            ans[p-1]=w[:-1]

        return " ".join(ans[:])