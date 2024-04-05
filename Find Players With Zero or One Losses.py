class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        won=[]
        lost=[]
        for i in range(0,len(matches)):
            won.append(matches[i][0])
            lost.append(matches[i][1])
        unique = []
        lost_set = set(lost)
        for k in won:
            if k not in lost_set:
                unique.append(k)
        
        count = Counter(lost)
        lost = [num for num in lost if count[num] == 1]
        unique=list(set(unique))
        unique.sort()
        lost.sort()
        ans = [unique, lost]
        return ans
