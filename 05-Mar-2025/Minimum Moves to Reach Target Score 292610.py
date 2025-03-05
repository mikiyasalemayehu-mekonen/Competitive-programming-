# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
      
        while maxDoubles!=0 and target!=1:
            if target%2==0:
                target = target//2
                count = count + 1
            else:
                target = target - 1
                target = target//2
                count = count + 2
            maxDoubles = maxDoubles - 1
        count = count + (target -1 if target>1 else 0)
        return count 


