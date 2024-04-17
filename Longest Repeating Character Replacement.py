class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right=0
        max_len=0
        count={}
        for i in range(len(s)):
            count[s[i]]=1+count.get(s[i],0)
            if (i-right+1)-max(count.values())<=k:
                max_len=max(max_len,i-right+1)
            else:
                count[s[right]]-=1
                right+=1
        return max_len
