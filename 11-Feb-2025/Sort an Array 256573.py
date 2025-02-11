# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        maximum = max(nums)
        minimum = abs(min(nums))
        count = [0]*(maximum+abs(minimum)+1)
        for num in nums:
            count[num+minimum] = count[num+abs(minimum)] +1

        return [ i-minimum for i in range(len(count)) for k in range(count[i])]
        