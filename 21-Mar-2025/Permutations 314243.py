# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def backtrack(t,store):
            if len(store)==n:
                result.append(store[:])
            if t>n:
                return
            for i in range(n):
                if i!=t and nums[i] not in store:
                    store.append(nums[i])
                    backtrack(i,store)
                    store.pop()


        backtrack(-1,[])
        return result
        