"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        arr = sorted(intervals, key = lambda x: x.start)
        for i in range(len(arr) -1):
            if arr[i].end <= arr[i+1].start:
                continue
            else:
                return False
        return True