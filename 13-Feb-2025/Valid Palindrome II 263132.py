# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        delete = 0
        while left < right:
            # if s[left] != s[right] and delete<1:
            #     if s[right-1] and s[right-1]==s[left]:
            #         right = right - 1
            #     else:
            #         left = left + 1
            #     delete = 1
            # elif s[left] != s[right] and delete==1:
            #     return False
            
            
            # else:
            #     left = left + 1
            #     right = right -1
            if s[left] != s[right]:
                s_1, s_2 = s[left+1:right+1], s[left:right]
                return s_1 == s_1[::-1] or s_2 == s_2[::-1]
            left += 1
            right -= 1
        return True
        