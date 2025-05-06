# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        root = {i:i for i in range(1,n+1)}
        size = [None]+[1]*n

        def find(x):
            if root[x]!=x:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x != parent_y:
                if size[parent_x] >= size[parent_y]:
                    root[parent_y] = parent_x
                    size[parent_x] += size[parent_y ]
                else:
                    root[parent_x] = parent_y
                    size[ parent_y ] += size[ parent_x ]
            else:
                return True
            
        ans =[ ]
        for  u,v in edges:
            temp = union(u,v)
            if temp:
                ans.append(u)
                ans.append(v)
        return ans
