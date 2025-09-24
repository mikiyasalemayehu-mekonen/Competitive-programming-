# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        def dp(i, holding):
            if i >= n:
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]
            res = 0
            if holding == 0:
                buy = dp(i + 1, 1) - prices[i]
                skip = dp(i + 1, 0)
                res = max(buy, skip)           
            else: 
                sell = dp(i + 2, 0) + prices[i] 
                hold = dp(i + 1, 1)
                res = max(sell, hold)             
            memo[(i, holding)] = res
            return memo[(i, holding)]
        
        return dp(0, 0)

          
            # else:
            #     # Option 1: sell today
            #     sell = dp(i + 1, 0) + prices[i]
            #     # Option 2: hold
               

