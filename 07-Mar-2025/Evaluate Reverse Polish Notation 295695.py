# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ('+', '-', '*',  '/')
        ans = 0
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                ans = 0
                if tokens[i]=="+":
                    ans = num1 + num2
                elif tokens[i]=="-":
                    ans = num2 - num1
                elif tokens[i]=="*":
                    ans = num2 * num1
                elif tokens[i]=="/" and num1!=0:
                    ans = int(num2 / num1)

                
                stack.append(ans)
  

        return stack[-1]
                
        