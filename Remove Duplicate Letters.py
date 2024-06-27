class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        seen=set()
        last={c:i for i,c in enumerate(s)}
        for i,c in enumerate(s):
            if c not in seen:
                while stack and (stack[-1]>c and last[stack[-1]]>i):
                    seen.remove(stack.pop())
                stack.append(c) 
                seen.add(c)
        return "".join(stack)
        
