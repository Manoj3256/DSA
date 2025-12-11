class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        d={}
        for w in words:
            d[int(w[-1])]=(w[:-1]+" ")
        a=""
        i=1
        while i<=len(d):
            if i==len(d):
                a+=d[i][:-1]
            else:
                a+=d[i]
            i+=1
        return a