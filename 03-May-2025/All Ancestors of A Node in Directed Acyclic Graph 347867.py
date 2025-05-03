# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)

        ans = []

        def bfs(start):
            visited = set()
            queue = deque()
            queue.append(start)
            ancestors = set()

            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        ancestors.add(nei)
                        queue.append(nei)
            return sorted(ancestors)

        for i in range(n):
            ans.append(bfs(i))

        return ans
     