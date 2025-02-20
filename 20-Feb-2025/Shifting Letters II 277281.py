# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)
        s = [ord(c) - 97 for c in s]

        for i in range(len(shifts)):
            if shifts[i][2] == 0:
                prefix[shifts[i][0]] -= 1
                prefix[shifts[i][1] + 1] += 1
            elif shifts[i][2] == 1:
                prefix[shifts[i][0]] += 1
                prefix[shifts[i][1] + 1] -= 1
                
        for k in range(1,len(prefix)):
           prefix[k] = prefix[k-1] + prefix[k]
        
        # print(prefix)
        for i in range(len(s)):
            s[i] = ((s[i] + prefix[i]) % 26) + 97
        return "".join(chr(c) for c in s)

        