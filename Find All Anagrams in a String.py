
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        count=Counter(p)
        temp=Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            temp[s[i]]+=1
            if temp==count:
                ans.append(i+1-len(p))
            temp[s[i+1-len(p)]]-=1
            if temp[s[i+1-len(p)]] == 0:
                temp.pop(s[i+1-len(p)])
        return ans
