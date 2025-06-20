# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def check(k):
            n = len(nums)
            q =[ 0 for i in range(n) ]
            for i in range(k):
                l, r, m = queries[i]
                q[l] -= m
                if r + 1 <n:
                    q[r + 1] += m

            for i in range(1, n ):
                q[i] += q[i - 1]
            
            for i in range(n):
                if nums[i] + q[i]>0:
                    return False
            return True
        left = 0
        right = len(queries)
        ans = -1
        while left<=right:
            mid = (left+right)//2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1


        return ans
