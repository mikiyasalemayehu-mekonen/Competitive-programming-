class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        current_score = 0
        
        for c in s:
            if c == '(':
                stack.append(current_score)
                current_score = 0
            else:
                current_score += stack.pop() + max(current_score, 1)
        
        return current_score
