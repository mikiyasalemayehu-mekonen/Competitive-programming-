class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}
        for i in range(len(s)):
            last_occurrence[s[i]] = i
        ans=[]
        size=0
        end=0
        for i in range(len(s)):
            size+=1
            end=max(last_occurrence[s[i]],end)
            if i==end:
                ans.append(size)
                size=0
        return ans
                
