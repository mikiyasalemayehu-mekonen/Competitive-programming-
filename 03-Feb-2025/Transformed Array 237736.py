# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result=[]
        length=len(nums)
        for i in range(length):
            if nums[i]==0:
                result.append(nums[i])
            # elif nums[i]>0:
            else:
                    temp=(nums[i]+i)%length   
                    result.append(nums[temp])
            # else:
            #     temp=abs(nums[i])%length 
            #     result.append(nums[temp-i])
        return result
        