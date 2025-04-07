# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2**n - 1
        def helper (length,k):
            if length==1:
                return "0"
            mid = (length)//2
            if mid==k-1:
                return "1"
            elif mid>k-1:
                return helper(mid,k)
            else:
                res = helper(mid,1+length-k)
                return "0" if res=="1" else "1"
        return helper(length,k)
        