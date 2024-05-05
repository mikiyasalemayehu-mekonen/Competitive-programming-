class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for temp in tokens:
            if temp == '+' or temp == '-' or temp == '*' or temp == '/':
                temp2 = int(stack.pop())
                temp3 = int(stack.pop())
                if temp == '+':
                    stack.append(temp3 + temp2)
                elif temp == '-':
                    stack.append(temp3 - temp2)
                elif temp == '*':
                    stack.append(temp3 * temp2)
                elif temp == '/':
                    stack.append(int(temp3 / temp2))  
            else:
                stack.append(int(temp))
        return stack[0]
