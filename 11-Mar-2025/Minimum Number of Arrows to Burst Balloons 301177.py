# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])

        count = 1  
        shotpoint = points[0][1] 
        for i in range(1, len(points)):
            if shotpoint < points[i][0]:  
                count += 1
                shotpoint = points[i][1] 

        return count
