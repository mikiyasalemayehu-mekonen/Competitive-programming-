# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        tem = 0
        l = 0
        count = 0
        for i in range(1,len(nums)):
            tem = tem |nums[i-1]
            if tem &nums[i] == 0:
                count = max(count,i-l+1)
            while  l<i and tem&nums[i] != 0:
                tem = tem^nums[l]
                l+=1        

        return count if count >0 else 1
