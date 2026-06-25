class Twitter:

    def __init__(self):
        self.clock = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.clock +=1
        self.tweets[userId].append((self.clock,tweetId))
       


    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        used = set()
        for tweetId in self.tweets[userId]:
            if tweetId not in used:
                heapq.heappush_max(heap,tweetId)
                used.add(tweetId)
        
        for user in self.following[userId]:
            for tweetId in self.tweets[user]:
                if tweetId not in used:
                    heapq.heappush_max(heap,tweetId)
                    used.add(tweetId)
        
        ct = 0
        fin = []
        while ct < 10 and heap:
            popped = heapq.heappop_max(heap)
            tweetId = popped[1]
            fin.append(tweetId)
            ct +=1
        return fin

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        try:
            self.following[followerId].remove(followeeId)
        except:
            return None
