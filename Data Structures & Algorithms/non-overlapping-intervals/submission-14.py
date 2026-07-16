class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        total = 0
        lastEnd = intervals[0][1]
        print(intervals)
        for i in range(1,len(intervals)):
            if intervals[i][0] < lastEnd:
                lastEnd = min(lastEnd, intervals[i][1])
                total += 1
            else:
                lastEnd = intervals[i][1]
        return total