# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        index = 0
        while index<length-1:
            far = index + nums[index] if index + nums[index]<length else length - 1
            maximum = far 
            max_index = far
            for i in range(index+1,far+1) :
                temp = i + nums[i]
                if temp > maximum:
                    maximum = temp
                    max_index = i
            index = max_index
            if nums[index]==0 and index!=length-1:
                return False
            
        return True

        