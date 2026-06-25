class MedianFinder:

    def __init__(self):
        self.leftSide  = []
        self.rightSide = []
        

    def addNum(self, num: int) -> None:
        l = self.leftSide
        r = self.rightSide

        if len(l) == len(r):
            if r:
                if num < l[0]:
                    heapq.heappush_max(l,num)
                else: 
                    heapq.heappush(r,num)
            else:
                heapq.heappush(r,num)
        elif len(l) > len(r):
            if num < l[0]:
                popped = heapq.heappop_max(l)
                heapq.heappush(r,popped)
                heapq.heappush_max(l,num)
            else:
                heapq.heappush(r,num)
        else:
            if num > r[0]:
                popped = heapq.heappop(r)
                heapq.heappush_max(l,popped)
                heapq.heappush(r,num)
            else:
                heapq.heappush_max(l,num)
        
        

    def findMedian(self) -> float:
        l = self.leftSide
        r = self.rightSide

        
        if len(r) == len(l):
            return (l[0] + r[0])/2
        elif len(l) > len(r):
            return l[0]
        else:
            return r[0]

        
        