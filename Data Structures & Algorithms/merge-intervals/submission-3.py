class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval: interval[0])
        prev_s = intervals[0][0]
        prev_e = intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if start > prev_e:
                res.append([prev_s, prev_e])
                prev_s = start
                prev_e = end
            # ext
            else:
                prev_e = max(prev_e, end)

        res.append([prev_s, prev_e])
        

        return res