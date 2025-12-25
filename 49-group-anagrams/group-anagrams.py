class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for i in strs:
            sortedlist = ''.join(sorted(i))
            if sortedlist in dic:  
                dic[sortedlist].append(i)
            else:
                dic[sortedlist] = [i]
                
        return list(dic.values()) 