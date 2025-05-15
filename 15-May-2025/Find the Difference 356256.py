# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tem = []
        xor = ord(t[0])
        for i in range(1,len(t)):
            xor = xor ^ ord(t[i])

        for x in s:
            xor = xor ^ ord(x)
            
        return chr(xor)
        