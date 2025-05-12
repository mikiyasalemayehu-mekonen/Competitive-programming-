# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-(i) for i in piles]
        heapify(piles)
        for t in range(k):
            heapreplace(piles, piles[0]//2)
        return -sum(piles)

        