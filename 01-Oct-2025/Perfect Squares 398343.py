# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = []
        for i in range(1, int(math.sqrt(n))+1):
            perfect_squares.append(i * i)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1,n+1):
            for square in perfect_squares:
                if i - square >= 0:
                    dp[i] = min(dp[i], dp[i - square] + 1)
                else:
                    break 
        return dp[n]



        