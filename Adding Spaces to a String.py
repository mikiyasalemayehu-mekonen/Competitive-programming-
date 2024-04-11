class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        temp=0
        for i in range(len(spaces)):
            index = spaces[i]
            ans += s[temp:index] + " " 
            temp=index
        ans+=s[temp:]
        return ans
        
