# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        maxi = 0
        for k,v in counter.items():
            if v%2==0:
                res = res + v
            else:
                if v>maxi:
                    res = res + maxi - 1 if maxi>0 else res
                    maxi = v
                else:
                    res = res + v - 1
        return res+maxi