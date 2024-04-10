class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans=0
        first=0
        last=len(skill)-1
        skill.sort()
        sum1=skill[first]+skill[last]
        while first<last:
            if sum1==skill[first]+skill[last]:
                ans=ans+skill[first]*skill[last]
                first+=1
                last-=1
            else:
                return -1
        return ans


        
