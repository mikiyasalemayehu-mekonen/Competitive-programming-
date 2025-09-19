# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)   
        stack = []

        for c in s:
            count[c] -= 1   
            if c in stack:
                continue
            while stack and stack[-1] > c and count[stack[-1]] > 0:
                removed = stack.pop()
            stack.append(c)
        return "".join(stack)
