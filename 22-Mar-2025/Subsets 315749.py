# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def backtrack(i,store):
            if i>n:
                return 
            result.append(store[:])
            for j in range(i,n):
                store.append(nums[j])
                backtrack(j+1,store)
                store.pop()
        backtrack(0,[])
        return result