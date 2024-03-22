class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        retu=strs[0]
        for j in range(1,len(strs)):
            temp=strs[j]
            for k in range(0,len(retu)):
                if k >= len(temp) or retu[k] != temp[k]:
                    retu = retu[:k]
                    break
        return retu
