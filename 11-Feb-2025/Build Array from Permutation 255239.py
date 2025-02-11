# Problem: Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        zero = 1
        for i in range(len(nums)):
            if nums[i] > 0 and (zero | nums[i] ):
                start = i
                res = nums[start]
                if nums[i]==0 :
                    zero = 0
                while nums[i] != start:
                    if nums[i]==0 :
                        zero = 0
                    temp = nums[i]
                    nums[i] = -1 * nums[nums[i]]
                    i = temp

                nums[i] = -1 * res

        for i in range(len(nums)):
            nums[i] *= -1

        return nums



        