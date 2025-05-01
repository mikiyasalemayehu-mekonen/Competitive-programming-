# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-(i) for i in stones]
        heapify(stones)
        while stones:
            
            if len(stones)>=2:
                x = -(heapq.heappop(stones))
                y = -(heapq.heappop(stones))
                if x!=y:
                    temp = abs(y - x)
                    heapq.heappush(stones,-(temp))
            else:
                return -(stones[0])
        return 0
            