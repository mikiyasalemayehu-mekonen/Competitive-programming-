# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            
            if s[i]=="]":
                string = []
                while stack and stack[-1]!="[":
                    string.append(stack[-1])
                    stack.pop()
                stack.pop()
                string.reverse()
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack[-1])
                    stack.pop()
                # if stack and stack[-1]=="[":
                #     stack.pop()
                num.reverse()
               
                num = "".join(num)
                string = "".join(string)
                ans = int(num) * string
                stack.append(ans)

            else:
                stack.append(s[i])

            print(stack)
        return "".join(stack)
            