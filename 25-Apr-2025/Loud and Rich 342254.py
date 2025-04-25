# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        n  = len(quiet)
        for u,v in richer:
            graph[v].append(u)
        res = [0]*n
        def bfs(t):
            nonlocal res
            visited = set()
            queue = deque()
            queue.append(t)
            mini = t
            while queue:
                temp = queue.popleft()
                for u in graph[temp]:
                    if u not in visited:
                        queue.append(u)
                        if quiet[u]<quiet[mini]:
                            mini = u
                        visited.add(u)
            res[t] = mini
                
        for i in range(n):
            bfs(i)
        return res

        