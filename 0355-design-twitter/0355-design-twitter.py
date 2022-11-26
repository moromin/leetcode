class Twitter:
    class LinkedList:
        def __init__(self, tweetId = None, userId = None):
            self.tweetId = tweetId
            self.userId = userId
            self.next = None

        def addToNext(self, new):
            next = self.next
            self.next = new
            new.next = next

    def __init__(self):
        self.userFollows = defaultdict(set)
        self.head = self.LinkedList()
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        new = self.LinkedList(tweetId, userId)
        self.head.addToNext(new)

    def getNewsFeed(self, userId: int) -> List[int]:
        userIds = self.userFollows[userId]
        userIds.add(userId)
        
        head = self.head.next
        count = 0
        res = []
        while head and count < 10:
            if head.userId in userIds:
                res.append(head.tweetId)
                count += 1
            head = head.next
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollows[followerId]:
            self.userFollows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)