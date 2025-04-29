# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-(i) for i in piles]
        heap =  [ ]
        for i in piles:
            heapq.heappush(heap, i)
        while k>0:
            temp = -(heapq.heappop(heap))
            temp = temp - (temp//2)
            heapq.heappush(heap,-(temp))
            k = k - 1
        return -(sum(heap))

        