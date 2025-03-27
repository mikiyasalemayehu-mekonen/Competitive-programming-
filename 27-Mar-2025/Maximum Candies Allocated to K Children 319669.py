# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(n):
            count = 0
            for i in range(len(candies)):
                if candies[i]>=n:
                    count = count + math.floor(candies[i]/n)
            return count>=k

        if sum(candies)<k:
            return 0
        low = 1
        high = max(candies)
        ans  = 0 
        while low<=high:
            mid = (high + low)//2
            if check(mid):
                ans = max(ans,mid)
                low = mid + 1
            else:
                high = mid - 1
        return ans
                