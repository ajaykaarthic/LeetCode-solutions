class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        
        # Loop through stock prices from day 2 for selling
        for r in range(1,len(prices)):
            # We want to the buy the stock at the lowest value
            # this logic will help us solve the problem in linear time
            if (prices[r] < prices[l]):
                l = r
            max_profit = max(max_profit, prices[r] - prices[l])
        return max_profit

# run time
# O(n)
       