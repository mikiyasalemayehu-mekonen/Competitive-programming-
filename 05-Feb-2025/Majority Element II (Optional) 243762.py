# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        more = []
        for key,value in count.items():
            length=len(nums)/3
            if value>length:
                more.append(key)
        return more

