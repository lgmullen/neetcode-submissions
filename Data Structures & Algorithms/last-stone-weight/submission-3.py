class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we need to get the two heaviest stones
        maxheap = []
        heapq.heapify(maxheap)
        # created the heap
        for stone in stones: 
            heapq.heappush(maxheap, -stone)
        
        while len(maxheap) >= 2:
            stone1 = heapq.heappop(maxheap) * -1
            stone2 = heapq.heappop(maxheap) * -1
            if stone1 == stone2:
                continue
            else:
                heapq.heappush(maxheap, (stone2 - stone1))
        if not maxheap:
            return 0
        return -maxheap[0]
