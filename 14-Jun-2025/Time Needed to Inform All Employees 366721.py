# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = [[] for _ in range(n)]  
        for i in range(n):
            if manager[i] != -1:
                subordinates[manager[i]].append(i)  
        def dfs(employee):
            max_time = 0  
            for subordinate in subordinates[employee]:
                max_time = max(max_time, informTime[employee] + dfs(subordinate))
            return max_time
    
        return dfs(headID)