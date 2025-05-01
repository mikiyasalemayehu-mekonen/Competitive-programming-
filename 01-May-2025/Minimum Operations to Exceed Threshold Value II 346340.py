# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        count = 0
        if nums[0]>=k:
            return 0

        while nums:
            x = heappop(nums)
            y = heappop(nums)
            temp = (min(x, y) * 2 + max(x, y))
            heappush(nums,temp)
            count = count + 1
            if nums[0] >=k:
                return count
