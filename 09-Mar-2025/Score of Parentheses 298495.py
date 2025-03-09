# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
            else:
                c = 0
                while stack[-1] != '(':
                    c += stack[-1]
                    stack.pop()
                stack.pop()    

                if not c:
                    c = 1
                    stack.append(c)
                else:
                    stack.append(c*2)

        return sum(stack)                 

        