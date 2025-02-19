# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
  
        count_ones = {"1":s.count("1")}
        count_zeroes = 0
        maximum = 0

        for i in range(len(s)-1):
            if s[i]=="0":
                count_zeroes = count_zeroes  + 1
            else:
                count_ones["1"] = count_ones["1"] - 1  

            maximum = max(maximum,count_zeroes+count_ones["1"])
    
        return maximum



        