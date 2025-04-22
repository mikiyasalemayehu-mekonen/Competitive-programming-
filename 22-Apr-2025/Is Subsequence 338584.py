# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr2 = 0
        if len(s)==1 and s[0] not in t:
            return False
        for c in s:
            if ptr2==len(t):
                return False

            while ptr2<len(t) and c!=t[ptr2]:
                ptr2 = ptr2 + 1
                if ptr2==len(t):
                    return False
            ptr2 = ptr2 + 1

        return True
        