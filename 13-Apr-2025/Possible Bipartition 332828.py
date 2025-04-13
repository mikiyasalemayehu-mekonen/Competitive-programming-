# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u,v in dislikes:
            adj[u].append(v)    
            adj[v].append(u)   
        group = {i:None for i in range(1,n+1)}
        def dfs(node,g):
            if not group[node]:
                group[node] = g
            else:
                return group[node] == g
            for peps in adj[node]:
                if not dfs(peps,1-g):
                    return False
            return True
        for peps in group:
            if not group[peps] and not dfs(peps,0):
                return False
        return True
        
