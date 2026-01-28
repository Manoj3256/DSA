class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        maxfreq=0
        freq=Counter(tasks)
        maxfreq=max(freq.values())
        maxCount=sum(1 for v in freq.values()if v == maxfreq)
        return max(len(tasks), (maxfreq-1)*(n+1)+maxCount )