# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        sum = 0
        index = 1
        for _ in range(len(piles)//3):
            sum += piles[index]
            index+=2
        return sum
        