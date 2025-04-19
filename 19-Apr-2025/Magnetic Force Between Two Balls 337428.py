# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        from typing import List
        position.sort()
        
        def canPlaceBalls(min_dist):
            count = 1
            last_pos = position[0]
            for i in range(1, len(position)):
                if position[i] - last_pos >= min_dist:
                    count += 1
                    last_pos = position[i]
                    if count == m:
                        return True
            return False
        
        left, right = 1, position[-1] - position[0]
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return result
