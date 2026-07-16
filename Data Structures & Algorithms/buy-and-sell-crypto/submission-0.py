class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # one day to buy it 1 day to sell
        low = prices[0]
        profit = 0
        for price in prices:
            low = min(low, price)
            profit = max(profit, price-low)
        return profit