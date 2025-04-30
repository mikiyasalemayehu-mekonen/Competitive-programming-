# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []

        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]

            if diff > 0:
                heapq.heappush(heap, diff)
            if len(heap) > ladders:
                smallest = heapq.heappop(heap)
                bricks -= smallest

            if bricks <0 and len(heap)==ladders:
                return i

        return len(heights) - 1
