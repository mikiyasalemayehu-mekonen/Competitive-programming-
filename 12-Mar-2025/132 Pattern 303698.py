# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        minimum = [nums[0]]
        for i in range(1, len(nums)):
            minimum.append(min(minimum[-1], nums[i])) 
        stack =[ ]
        for j in range(len(nums) - 1, 0, -1):
            if nums[j] > minimum[j - 1]:  
                while stack and stack[-1] <= minimum[j - 1]:  
                    stack.pop()  
                if stack and stack[-1] < nums[j]:  
                    return True 
                stack.append(nums[j]) 
        
        return False

