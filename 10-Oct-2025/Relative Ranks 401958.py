# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = [-x for x in score]
        heapq.heapify(s)
        rank = 1
        place = {1:"Gold Medal",2:"Silver Medal",3:"Bronze Medal"}
       
        while s:
            val = -heapq.heappop(s)  
            idx = score.index(val)   
            if rank in place:
                score[idx] = place[rank]
            else:
                score[idx] = str(rank)
            rank += 1
        return score