
class Twitter:

    def __init__(self):
        self.following = defaultdict(set) # (userID -> [followee1, followee2...])
        self.tweets = defaultdict(list) # (userID -> [tweets])\
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        idx = len(self.tweets[userId])
        self.tweets[userId].append((-self.time, tweetId, userId, idx))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = set(self.following.get(userId, set()))
        users.add(userId)

        heap = []
        for uid in users:
            if self.tweets[uid]:
                heap.append(self.tweets[uid][-1])

        heapq.heapify(heap)

        feed = []
        while heap and len(feed) < 10:
            _, tweetId, uid, idx = heapq.heappop(heap)
            feed.append(tweetId)
            if idx > 0:
                heapq.heappush(heap, self.tweets[uid][idx - 1])
            

        return feed

        return 
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
