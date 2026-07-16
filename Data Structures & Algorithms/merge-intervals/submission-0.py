class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval: interval[0])

        res = []
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start > prev_end:
                res.append([prev_start, prev_end])
                prev_start = start
                prev_end = end
            else:
                prev_end = max(prev_end, end)
                
        res.append([prev_start, prev_end])
            
            
        return res       