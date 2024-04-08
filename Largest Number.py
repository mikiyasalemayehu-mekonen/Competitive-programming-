
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largestnumber =''
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                temp1 = str(nums[i])+str(nums[j])
                temp2 = str(nums[j])+str(nums[i])
                if int(temp2) > int(temp1):
                    nums[i] , nums[j] = nums[j] , nums[i]
        for i in range(len(nums)):
            largestnumber += str(nums[i])
        return str(int(largestnumber))
