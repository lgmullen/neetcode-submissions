class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            # dont do anything
            skip = dfs(i+1, canBuy)

            if canBuy:
                buy = dfs(i+1, False) - prices[i]
                ans = max(skip, buy)

            else:
                sell = dfs(i+2, True) + prices[i]
                ans = max(sell, skip)
            dp[(i, canBuy)] = ans
            return ans


        return dfs(0, True)
