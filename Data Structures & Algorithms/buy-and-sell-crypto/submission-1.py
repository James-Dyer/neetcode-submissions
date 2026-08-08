class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0

        for sell in range(len(prices)):
            if prices[sell] > prices[buy]:
                curr_profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, curr_profit)
            else:
                buy = sell

        return max_profit