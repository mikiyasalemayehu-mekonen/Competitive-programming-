# Problem: Vowels of All Substrings - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        res = 0
        memo = {}

        def dp(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            cnt = dp(i + 1)
            if word[i] in vowels:
                cnt += (n - i)
            memo[i] = cnt
            return  memo[i]

        for i in range(n):
            res += dp(i)

        return res
