# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terminal = []
        outdegree = [0]*len(graph)
        for i in range(len(graph)):
            if not graph[i]:
                terminal.append(i)
            outdegree[i] = len(graph[i])

        adj = defaultdict(list)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                adj[graph[i][j]].append(i)
        
     
        queue = deque(terminal)
        while queue:
            temp = queue.popleft()
            for u in adj[temp]:
                outdegree[u] =  outdegree[u] - 1
                if  outdegree[u] ==0:
                    terminal.append(u)
                    queue.append(u)

        return sorted(list(terminal))
        