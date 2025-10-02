# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        memo = {}
        
        def dp(i, holding):
            if i == n:
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]
            if holding == 0: 
                include = dp(i + 1, 1) - prices[i]  
                exclude = dp(i + 1, 0)            
            else: 
                include = dp(i + 1, 0) + prices[i] - fee  
                exclude = dp(i + 1, 1)                    
            memo[(i, holding)] = max(include, exclude)
            return memo[(i, holding)]
        
        return dp(0, 0)