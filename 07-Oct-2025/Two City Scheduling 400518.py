# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/



class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sorted_costs = sorted(costs, key=lambda x: x[0] - x[1])
        
        n = len(costs)
        a_total = sum(x[0] for x in sorted_costs[:n // 2])  
        b_total = sum(x[1] for x in sorted_costs[n // 2:])  
        return a_total + b_total
