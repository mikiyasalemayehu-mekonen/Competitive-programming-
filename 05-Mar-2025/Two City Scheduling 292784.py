# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort based on the difference between cost to A and cost to B
        costs.sort(key=lambda x: x[0] - x[1])
        
        total_cost = 0
        n = len(costs) // 2
        
        # First half goes to city A, second half to city B
        for i in range(n):
            total_cost += costs[i][0]  # Send first half to city A
        for i in range(n, 2 * n):
            total_cost += costs[i][1]  # Send second half to city B
        
        return total_cost
