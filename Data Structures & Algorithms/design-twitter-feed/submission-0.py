
class Twitter:

    def __init__(self):
        self.following = defaultdict(set) # (userID -> [followee1, followee2...])
        self.tweets = defaultdict(list) # (userID -> [tweets])\
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = set(self.following.get(userId, set()))
        users.add(userId)

        feed = []

        for uid in users:
            feed.extend(self.tweets.get(uid, []))

        feed.sort(reverse=True)

        return [tweetId for _, tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
