# Problem: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxi = deque()
        mini = deque()
     
        n =len(nums)
        res = 0  
        left = 0  
        for right, num in enumerate(nums):
            while maxi and nums[maxi[-1]] < num:
                maxi.pop()
            maxi.append(right)


            while mini and nums[mini[-1]] > num:
                mini.pop()
            mini.append(right)

            while abs(nums[maxi[0]]-nums[mini[0]])>limit:
                if maxi[0]==left:
                    maxi.popleft()
                if mini[0]==left:
                    mini.popleft()
                left = left + 1

            
            res = max(right-left+1,res)
        return res


