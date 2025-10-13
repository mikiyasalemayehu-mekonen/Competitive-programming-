# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 == 0:
            return True 

        total = sum(nums)
        target = math.ceil(total / 2)

        memo = {}

        def dp(i, j, turn):
            if i > j:
                return 0

            if (i, j, turn) in memo:
                return memo[(i, j, turn)]

            if turn:  
                first = nums[i] + dp(i + 1, j, False)
                last = nums[j] + dp(i, j - 1, False)
                res = max(first, last)
            else: 
                first = dp(i + 1, j, True)
                last = dp(i, j - 1, True)
                res = min(first, last)

            memo[(i, j, turn)] = res
            return res

        player1_score = dp(0, n - 1, True)
        return player1_score >= target

        