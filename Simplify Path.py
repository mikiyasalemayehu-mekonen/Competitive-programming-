class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        path=path.split("/")
        for temp in path:
            if temp=="..":
                if stack:
                    stack.pop()
            elif temp!="." and temp!="" :
                stack.append(temp)
           
        return "/"+"/".join(stack)

        
