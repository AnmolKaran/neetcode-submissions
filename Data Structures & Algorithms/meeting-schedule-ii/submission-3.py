"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        intervals = sorted(intervals,key = lambda k: k.start)
        if not intervals:
            return 0
        heapq.heappush(heap,intervals[0].end)
        for i in range(1, len(intervals)):
            startTime = intervals[i].start
            if startTime < heap[0]:
                heapq.heappush(heap,intervals[i].end)

            else:
                heapq.heappop(heap)
                heapq.heappush(heap,intervals[i].end)
        return len(heap)