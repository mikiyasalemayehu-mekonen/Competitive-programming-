# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        n  = len(questions)
        def dp(i):
          
            if i>=n:
                return 0
       
            if i in memo:
                return memo[i]
            take = questions[i][0] + dp(i+questions[i][1]+1)
            not_take = dp(i+1)
            ans = max(take,not_take)
            memo[i] = ans
        
            return memo[i]
      
        return  dp(0)
        