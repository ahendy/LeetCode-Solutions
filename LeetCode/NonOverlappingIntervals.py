# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals or len(intervals) == 1:
            return 0
            
        intervals = iter(sorted(intervals, key=lambda x: (x.start, x.end)))
        maxend = next(intervals).end
        count = 0

        for interval in intervals:
            if interval.start < interval.end < maxend:
                count += 1
                maxend = interval.end
            
            elif interval.start < maxend:
                count += 1
            
            else:
                maxend = interval.end
                
        return count
                
                
            
