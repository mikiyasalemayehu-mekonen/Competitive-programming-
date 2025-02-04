# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count=Counter(nums)
        for value in count.values():
            if value>=2:
                return True
        return False
        