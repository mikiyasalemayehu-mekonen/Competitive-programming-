# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_adj = defaultdict(list)
        for u,v in redEdges:
            red_adj[u].append(v)
        
        blue_adj = defaultdict(list)
        for u,v in blueEdges:
            blue_adj[u].append(v)

        ans = [0]*(n)
        def bfs( n,blu):
            red_visited = set()
            blu_visited = set()
            if blu:
                blu_visited.add(0)
            else:
                red_visited.add(0)


            queue = deque()
            count = 0
            queue.append(0)
            while queue:
                length = len(queue)
                for i in range(length):
                    t = queue.popleft()
                    if blu:
                        if t in blue_adj:
                            for x in blue_adj[t]:
                                if x==n:
                                    return count + 1
                                if x not in blu_visited:
                                    blu_visited.add(x)
                                    queue.append(x)

                    else:
                        if t  in red_adj:
                            for x in red_adj[t]:
                                if x==n:
                                    return count + 1
                                if x not in red_visited :
                                    red_visited.add(x)
                                    queue.append(x)
                count = count + 1
                blu = not blu
            return -1


        for i in range(1,n):
            temp1 = bfs(i,True)
            temp2 = bfs(i,False)
            if temp1==-1 or temp2==-1:
                ans[i] = max(temp1,temp2)

            else:
                ans[i] = min(temp1,temp2)

        return ans
        