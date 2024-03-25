class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
        for j in range(0, len(nums) - 1):
            if nums[j] == 0:
                for k in range(j + 1, len(nums)):
                    if nums[k] != 0:
                        nums[j], nums[k] = nums[k], nums[j]
                        break
                    else:
                        continue
        return nums
