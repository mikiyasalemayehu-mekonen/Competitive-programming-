# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(i,store):
            if len(store)==k:
                result.append(store[:])
            for j in range(i+1,n+1):
                store.append(j)
                backtrack(j,store)
                store.pop()

        backtrack(0,[])
        return result