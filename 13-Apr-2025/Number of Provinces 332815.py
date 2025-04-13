# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    adj[i+1].append(j+1)
        visited = set()
        def dfs(city):
            visited.add(city)
            for neighbour in adj[city]:
                if neighbour not in visited:
                    dfs(neighbour)
            return
        ans = 0 
        for i in range(1,n+1):
            if i not in visited:
                dfs(i)
                ans  = ans + 1
        return ans

    