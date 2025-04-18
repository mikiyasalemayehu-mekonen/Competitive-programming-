# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        def champ(i):
            visited = set()

            def dfs(node):
                visited.add(node)
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        dfs(neighbour)

            dfs(i)
            return len(visited) == n

        for i in range(n):
            if champ(i):
                return i
        return -1
