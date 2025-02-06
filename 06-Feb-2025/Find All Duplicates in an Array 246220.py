# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        twice=[]
        count=Counter(nums)
        for key,value in count.items():
                if value==2:
                    twice.append(key)
        return twice 
        