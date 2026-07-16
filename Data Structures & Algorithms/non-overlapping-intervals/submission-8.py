class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        total = 0
        lastEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start >= lastEnd:
                lastEnd = end
            else:
                total += 1
                lastEnd = min(end, lastEnd)
        return total