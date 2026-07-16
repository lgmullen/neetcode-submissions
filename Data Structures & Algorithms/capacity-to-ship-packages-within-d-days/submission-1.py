class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # calculate days per ship size
        def getdays(cap):
            d = 0
            total = 0
            for w in weights:
                total += w
                if total > cap:
                    total = w
                    d += 1
            if total != 0:
                d += 1
            return d
        
        l = max(weights)
        r = sum(weights)
        res = r
        while l <= r:
            cap = (l + r) // 2
            output = getdays(cap)
            print(cap, output)
            if output <= days:
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res
                
                

                
                
        
            
        