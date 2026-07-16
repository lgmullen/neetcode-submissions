class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        
        res = []
        intervals = sorted(intervals, key=lambda interval: interval[0])
        n = len(intervals)
        
        intervalStart = newInterval[0]
        intervalEnd = newInterval[1]
        i = 0
        # fine the beginning
        while i < n and intervals[i][1] < intervalStart:
            res.append(intervals[i])
            i+=1


        while i < n and intervals[i][0] <= intervalEnd:
        #merge this 
            intervalStart = min(intervalStart, intervals[i][0])
            intervalEnd = max(intervalEnd, intervals[i][1])
            i+=1
        print(intervalStart,intervalEnd)
        res.append([intervalStart,intervalEnd])
    
        while i < n:
            res.append(intervals[i])
            i+=1
        return res


        