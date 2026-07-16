class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval: interval[0])
        res = [intervals[0]]
        for i in range(len(intervals)):
            print(res)
            start, end = intervals[i][0], intervals[i][1]
            #compare to prev end
            if start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start,end])
                
            
            
        return res       