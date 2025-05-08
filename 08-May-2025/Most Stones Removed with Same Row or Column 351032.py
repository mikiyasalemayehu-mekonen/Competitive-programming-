# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        root = {i:i for i in range(len(stones))}
        size = [1]*len(stones)
        def get(x):
            if root[x]!=x:
                root[x] = get(root[x])
            return root[x]
        def union(x,y):
            parent_x = get(x)
            parent_y = get(y)
            if parent_x!=parent_y:
                if size[parent_x]>size[parent_y]:
                    size[parent_x] += size[parent_y]
                    root[parent_y] = parent_x
                else:
                    size[parent_y] += size[parent_x]
                    root[parent_x] = parent_y

        temp = defaultdict(list)
        for i in range(len(stones)-1):
            for j in range(i+1,len(stones)):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1] :
                    union(i,j)
        for i in range(len(stones)):
            get(i)
    
        return len(stones) - len(set(root.values()))
        


