# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n  = len(isConnected)
        adj = {}
        parent = [i for i in range(n)]
        size = [1] * n
        def find(x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]
		
        def union( x, y):
            parent_x = find(x)
            parent_y = find(y)
            if size[parent_x]>=size[ parent_y]:
                parent[parent_y] =  parent_x
                size[parent_x] =  size[parent_x] +  size[parent_y]
            else:
                parent[parent_x] =  parent_y
                size[parent_y] =  size[parent_y] +  size[parent_x]
        for  row in range(n):
            for col in range(n):
                if isConnected[row][col]==1 :
                    union(row,col)
        print(parent)

        root_set = set(find(i) for i in range(n))        
        return len(set(parent))

    