"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        events = []
        for x in intervals:
            events.append((x.start, 1))
            events.append((x.end, -1))

        events.sort()

        res = 0
        rooms_needed = 0

        for event in events:
            rooms_needed += event[1]
            res = max(res, rooms_needed)

        return res
