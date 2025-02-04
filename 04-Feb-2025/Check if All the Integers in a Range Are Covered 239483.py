# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums={j for r in ranges for j in range(r[0],r[1]+1)}
        for i in range(left, right+1):
            if i not in nums:
                return False
        return True

