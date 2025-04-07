# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(vertex,visited):
            if vertex==destination:
                return True
            visited.add(vertex)
            for gorebet in graph[vertex]:
                if gorebet not in visited:
                    if dfs(gorebet,visited):
                        return True
            return False
        
        return dfs(source,set())