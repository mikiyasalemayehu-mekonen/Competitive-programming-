# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = -1
        for i in range(len(nums)):
            if nums[i]==1:
                left = i
                break
        res= 0 
        for i in range(len(nums)):
            if nums[i]==1 and left!=-1:
                res = max(res,i-left + 1)
            elif left==-1 and  nums[i]==1 :
                res = max(res,1)
                left =  i
            else:
                left = -1
        return res
