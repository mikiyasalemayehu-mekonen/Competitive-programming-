# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        ans = 0
        low  = 0
        high = n
        def first(low,high):
            if low==high:
                return low 
            mid = (low+high)//2
            if isBadVersion(mid):
                return first(low,mid)
            else:
                return first(mid+1,high)
        return first(low,high)
        