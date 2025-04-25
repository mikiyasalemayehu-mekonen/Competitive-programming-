# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        n  = len(quiet)
        indegree =[0]*n
        for u,v in richer:
            graph[u].append(v)
            indegree[v] = indegree[v] + 1
        
        queue = deque()
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
        
        res = [ i for i in range(n)]
        while queue:
            for i in range(len(queue)):
                temp = queue.popleft()
                for u in graph[temp]:
                    if quiet[res[temp]] < quiet[res[u]]:
                        res[u] = res[temp]
                    indegree[u] = indegree[u] - 1
                    if indegree[u]==0:
                        queue.append(u)

                
        return res

        