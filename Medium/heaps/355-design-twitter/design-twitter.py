import heapq
from collections import defaultdict
class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heap=[]
        self.co=0
        self.dic=defaultdict(set)
    def postTweet(self,userId,tweetId):
        """
        Compose a new tweet.
        :type userId:int
        :type tweetId:int
        :rtype:None
        """
        heapq.heappush(self.heap,(-self.co,userId,tweetId))
        self.co+=1
    def getNewsFeed(self,userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        :type userId:int
        :rtype:List[int]
        """
        users={userId}
        users.update(self.dic[userId])
        top10=heapq.nsmallest(10,((c,t)for c,u,t in self.heap if u in users))
        return[t for c,t in top10]
    def follow(self,followerId,followeeId):
        """
        Follower follows a followee.
        :type followerId:int
        :type followeeId:int
        :rtype:None
        """
        if followerId!=followeeId:
            self.dic[followerId].add(followeeId)
    def unfollow(self,followerId,followeeId):
        """
        Follower unfollows a followee.
        :type followerId:int
        :type followeeId:int
        :rtype:None
        """
        self.dic[followerId].discard(followeeId)
# Your Twitter object will be instantiated and called as such:
# obj=Twitter()
# obj.postTweet(userId,tweetId)
# param_2=obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
