# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue = deque()
        min_queue = deque()  
        res = 0  
        left = 0  
        for right, num in enumerate(nums):
            while max_queue and nums[max_queue[-1]] < num:
                max_queue.pop()
            max_queue.append(right)

            while min_queue and nums[min_queue[-1]] > num:
                min_queue.pop()
            min_queue.append(right)

            while abs(nums[max_queue[0]] - nums[min_queue[0]]) > limit:
                if left == max_queue[0]:  
                    max_queue.popleft()
                if left == min_queue[0]:  
                    min_queue.popleft()
                left += 1  
            res = max(res, right - left + 1)

        return res 
