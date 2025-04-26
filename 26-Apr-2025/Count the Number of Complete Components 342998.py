# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def bfs(start):
            queue = deque([start])
            visited.add(start)
            nodes = 0
            edge_count = 0
            while queue:
                u = queue.popleft()
                nodes += 1
                edge_count += len(graph[u])
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)
            edge_count //= 2
            return nodes, edge_count

        ans = 0
        for i in range(n):
            if i not in visited:
                nodes, edge_count = bfs(i)
                if edge_count == nodes * (nodes - 1) // 2:
                    ans += 1
        return ans
