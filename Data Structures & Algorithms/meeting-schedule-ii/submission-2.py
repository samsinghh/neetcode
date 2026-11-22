"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        res, curr = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if starts[s] < ends[e]:
                s += 1
                curr += 1
            else:
                e += 1
                curr -= 1
            res = max(res, curr)
        return res