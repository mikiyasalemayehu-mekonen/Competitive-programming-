# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # for i in range(1,len(nums)):
        #     nums[i] = nums[i] + nums[i-1]
        left = 0
        # right = k-1
        # maximum = k
        zeros = 0
        maximum = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros  = zeros + 1
            while zeros>k and left<=i:
                if nums[left]==0:
                    zeros = zeros - 1
                left = left + 1
            maximum = max(maximum,i-left+1)

        return maximum
            


            
