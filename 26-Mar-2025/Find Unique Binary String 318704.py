# Problem: Find Unique Binary String - https://leetcode.com/problems/find-unique-binary-string/description/

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        k = len(nums[0])
        def backtrack(store,k):
            if len(store)==k:
                temp = "".join(store)
                if temp not in nums:
                    return temp
                return []
            for i in range(2):
                store.append(str(i))
                temp = backtrack(store,k)
                if not temp :
                    store.pop()
                else:
                    return temp
         
        return backtrack([],k)
        