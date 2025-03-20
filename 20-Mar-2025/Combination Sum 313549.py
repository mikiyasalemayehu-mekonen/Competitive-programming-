# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        def backtrack(i,store):
            if sum(store)==target and sorted(store) not in result:
                result.append(sorted(store[:]))
                return
            if sum(store)==target and sorted(store)  in result:
                return
            if sum(store)>target:
                return
            for j in range(n):
                store.append(candidates[j])
                backtrack(j+1,store)
                store.pop()
        backtrack(0,[])
        return result