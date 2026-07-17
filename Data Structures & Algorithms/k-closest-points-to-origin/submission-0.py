class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        res = []
        for x,y in points:
            distance = math.sqrt((0 - x) ** 2 + (0 - y) ** 2)
            heapq.heappush(minheap, (-distance, (x,y)))
            if len(minheap) > k:
                heapq.heappop(minheap)
        for i in range(k):
            x,y = heapq.heappop(minheap)[1]
            res.append([x,y])
        return res