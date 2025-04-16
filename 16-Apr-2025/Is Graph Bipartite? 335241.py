# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colour = [0] * n
        for node in range(n):
            if colour[node] != 0:
                continue
            queue = deque()
            queue.append(node)
            colour[node] = 1
            while queue:
                temp = queue.popleft()
                for u in graph[temp]:
                    if colour[u]==0:
                        colour[u] = -colour[temp]
                        queue.append(u)
                    elif colour[u]!=-colour[temp]:
                        return  False
        return True 



