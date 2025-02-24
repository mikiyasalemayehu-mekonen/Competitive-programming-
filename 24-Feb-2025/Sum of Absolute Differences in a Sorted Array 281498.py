# Problem: Sum of Absolute Differences in a Sorted Array - https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix_sum = [0] * length
        prefix_sum[0] = nums[0]
        
        for i in range(1, length):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        total_sum = prefix_sum[-1]
        result = [0] * length
        
        for i in range(length):
            left_sum = i * nums[i] - (prefix_sum[i - 1] if i > 0 else 0)
            right_sum = (total_sum - prefix_sum[i]) - (length - i - 1) * nums[i]
            result[i] = left_sum + right_sum
        
        return result
