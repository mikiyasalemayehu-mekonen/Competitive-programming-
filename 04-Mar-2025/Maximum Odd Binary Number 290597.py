# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        nums = list(s)
        count = Counter(nums)
        ans = []
        while count["1"]>1:
            ans.append("1")
            count["1"] = count["1"] - 1
        ans.extend([count["0"]*"0"])
        ans.append("1")
        return "".join(ans)