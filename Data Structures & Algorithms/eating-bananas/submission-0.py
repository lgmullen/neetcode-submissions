class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find the minimum speed (in bananas you must eat)
        # cant take more than h hours
        def eat_bananas(piles, bananas):
            total_hours = 0
            #calculate time to eat all of the piles
            for i in range(len(piles)):
                #banas in pile
                if bananas >= piles[i]:
                    total_hours += 1
                else:
                    total_hours += math.ceil(piles[i] / bananas)
            return total_hours
        
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            k = (right + left) // 2
            hours = eat_bananas(piles, k)
            if hours <= h:
                res = k
                right = k-1
            else:
                left = k+1
        return res