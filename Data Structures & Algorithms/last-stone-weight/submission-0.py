class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we need to get the two heaviest stones
        maxheap = []
        # heapq.heapify(maxheap)
        # created the heap
        for stone in stones: 
            heapq.heappush(maxheap, -stone)
        while len(maxheap) >= 2:
            # x
            stone_x = heapq.heappop(maxheap) * -1
            stone_y = heapq.heappop(maxheap) * -1

            if stone_x > stone_y:
                heapq.heappush(maxheap, (stone_x-stone_y) * -1)
        maxheap.append(0)
        return -(maxheap[0])     

