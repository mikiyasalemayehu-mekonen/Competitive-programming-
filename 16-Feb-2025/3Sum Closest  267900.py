# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # closest =
        closest_sum =  float("inf")
        for i in range(len(nums)-2):
            index1 = i + 1
            index2  = len(nums)-1
            while index1 <index2:
                current_sum = nums[i] + nums[index1] + nums[index2]
         
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    index1 += 1  
                elif current_sum > target:
                    index2 -= 1  
                else:
                    return current_sum  

        return closest_sum

  
        
            
