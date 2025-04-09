# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        first = employees[0].id
        e = defaultdict(list)
        values = dict()
        for emp in employees:
            e[emp.id] = emp.subordinates
            values[emp.id] = emp.importance
        visited = set()
        ans = 0
        def dfs(ids,visited):
            nonlocal ans
            visited.add(ids)
            ans = ans + values[ids]
            for num in e[ids]:
                if num not in visited:
                    dfs(num,visited)
        dfs(id,visited)
        return ans

        