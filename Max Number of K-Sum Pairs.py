class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        first = 0
        last = len(nums) - 1
        nums.sort()
        
        while first < last:
            if nums[first] + nums[last] == k:
                nums.pop(last)
                nums.pop(first)
                last -= 2
                ans += 1
            elif nums[first] + nums[last] >= k:
                last -= 1
            else:
                first += 1
        
        return ans
