# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest=0
        for money in accounts:
            richest=max(richest,sum(money))

        return richest