# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = 0
        right = n
        ans = []
        while left<n and right<n*2:
            ans.append(nums[left])
            ans.append(nums[right])
            left = left + 1
            right = right + 1
        return ans