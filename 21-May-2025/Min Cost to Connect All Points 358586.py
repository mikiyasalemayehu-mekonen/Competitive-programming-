# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i  in range(len(points)-1):
            for j in range(i+1,len(points)):
                val = abs(points[i][0]-points[j][0])  + abs(points[i][1]-points[j][1])
                edges.append((i,j,val))
        edges = sorted(edges,key=lambda x:x[2])
        parent = {i:i for i in range(n)}
        size = [-1]+[1]*n
        def get(x):
            if parent[x]!=x:
                x = get(parent[x])
            return x
        def union(x,y):
            parent_x = get(x)
            parent_y = get(y)
            if size[parent_x]>=size[parent_y]:
                parent[parent_y] = parent_x
                size[parent_x] = size[parent_x] + 1
            else:
                parent[parent_x] = parent_y
                size[parent_y] = size[parent_y] + 1
        mini = 0
        for u,v,a in edges:
            if get(u)!=get(v):
                union(u,v)
                mini = mini + a
        return mini
    #         edges.append((b,w,e))
        
    #     heap = []
    #     root = defaultdict(list)
    #     parent = [i for i in range(n)]
    #     ans = 0
    #     def get(x):
    #         if parent[x]!=x:
    #             parent[x] = get(parent[x])
    #         return parent[x]

    #     def union(x,y,z):
    #         par_x = get(x)
    #         par_y = get(y)
    #         if par_x!=par_y:
                
    #             parent[par_x] = par_y

       
    #     graph =  []
    #     for i in range(n-1):
    #         for j in range(i+1,n):
    #             x_dis = points[i][0] - points[j][0]
    #             y_dis = points[i][1] - points[j][1]
    #             graph.append(i,j,abs(x_dis)+abs(y_dis))
    #     graph.sort(key=lambda x:x[2])
    #     for u,v,z in graph:
    #         union(u,v,z)
    #     return ans
    #     def solve():
    # n, m = map_int()
    # edges = []
    # for i in range(m):
    #     b,w,e = map_int()
    #     edges.append((b,w,e))
   
