class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        
        res = []
        intervals = sorted(intervals, key=lambda interval: interval[0])
        n = len(intervals)

        intervalStart = newInterval[0]
        intervalEnd = newInterval[1]
        i = 0
        
        while i < n and intervals[i][1] < intervalStart:
            res.append([intervals[i][0], intervals[i][1]])
            i += 1
        

        newStart = min(intervals[i][0], intervalStart)

        # merge here
        newEnd = intervalEnd
        print(newEnd)
        while i < n and intervals[i][0] <= intervalEnd:
            newEnd = max(intervals[i][1], newEnd)
            i += 1
        res.append([newStart, newEnd])
        while i < n:
            res.append(intervals[i])
            i+=1

        return res




        