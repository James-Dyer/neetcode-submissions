"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval : interval.start)
        prev = None
        for interval in intervals:
            if prev and prev.end > interval.start:
                return False
            prev = interval
        
        return True