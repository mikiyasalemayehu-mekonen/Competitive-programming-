# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_R = 0
        count_L = 0
        maximum = 0
        for i in range(len(s)):
            if s[i]== "R":
                count_R = count_R + 1
            else:
                count_L = count_L + 1
            if count_L==count_R:
                maximum = maximum + 1
                count_R = 0
                count_L = 0
        return maximum

        