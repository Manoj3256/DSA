class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote)>len(magazine):
            return False
        maga={}
        for i in  magazine:
            if i in maga:
                maga[i]+=1
            else:
                maga[i]=1
        for i in ransomNote:
            if i in maga:
                if maga[i]>1:
                    maga[i]-=1
                else:
                    maga.pop(i)
            else:
                return False
        return True