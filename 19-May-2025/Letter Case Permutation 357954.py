# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        tem = ""
        ans = [ ]
        for i in range(len(s)):
            if s[i].isalpha():
                tem = tem + "0"
            else:
                tem = tem  + "1"

        
        def backtrack(n,stack):
            nonlocal ans
        
            if len(stack)==len(s):
                ans.append("".join(stack))
                # return
            for i in range(n,len(tem)):
                if tem[i]=="1":
                    stack.append(s[i])
                    backtrack(i+1,stack)
                    stack.pop()
                else:
                    stack.append(s[i])
                    backtrack(i+1,stack)
                    stack.pop()
                    stack.append(s[i].swapcase())
                    backtrack(i+1,stack)
                    stack.pop()
        backtrack(0,[])
        return ans 

