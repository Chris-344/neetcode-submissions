"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starting=[intervals[i].start for i in range(len(intervals))]
        ending=[intervals[i].end for i in range(len(intervals))]

        starting.sort()
        ending.sort()

        res=0
        s=e=0
        count=0
        while e<len(ending) and s<len(starting):
            if starting[s]<ending[e]:
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            res=max(res,count)
        return res