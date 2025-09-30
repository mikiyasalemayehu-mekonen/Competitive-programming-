# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        def dp(i,j,alice_w,bob_w,turn):
            if i>j:
                return alice_w>bob_w
            res = False
            if turn :
                alice_w += piles[i]
                res = res or dp(i+1,j,alice_w,bob_w,not turn)
                alice_w += piles[j]
                res = res or dp(i,j-1,alice_w,bob_w,not turn)
            else:
        
                bob_w += piles[i]
                res = res or dp(i+1,j,bob_w,bob_w,not turn)
                bob_w += piles[j]
                res = res or dp(i,j-1,alice_w,bob_w,not turn)

            return res

        
        res = dp(0,n-1,0,0,True)
        print(res)
       
        return res

        