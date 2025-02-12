# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i in range(1,len(costs)):
            costs[i] = costs[i] + costs[i-1]
    
        for i in range(len(costs)):
            if costs[i]== coins:
                return i+1
            elif costs[i]>coins:
                return i
            elif i+1<len(costs) and (costs[i] < coins and costs[i+1] >coins):
                return i+1
            elif i+1 ==len(costs):
                return len(costs)

























        
            
        