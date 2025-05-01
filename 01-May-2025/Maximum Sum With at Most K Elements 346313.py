# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        if k==0:
            return 0
        for i in  range(len(grid)):
            grid[i].sort(reverse=True)
            index = 0  
            for j in range(limits[i]):
                heappush(heap,grid[i][index])
                index = index + 1
            while len(heap)>k:
                heappop(heap)
        # print(heap)
        return sum(heap)
