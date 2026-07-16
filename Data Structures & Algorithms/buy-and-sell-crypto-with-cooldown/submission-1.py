class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            # dont do anything
            cooldown = dfs(i+1, canBuy)

            if canBuy:
                buy = dfs(i+1, False) - prices[i]

                # return this 
                dp[(i, canBuy)] = max(cooldown, buy)
                return dp[(i, canBuy)]
            else:
                sell = dfs(i+2, True) + prices[i]
                return max(sell, cooldown)


        return dfs(0, True)
