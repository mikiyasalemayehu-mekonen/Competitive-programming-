# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key =lambda x:x[1])
        n = len(points)
        first = points[0][1]
        res = 1
        for i in range(1,n):
            if first<points[i][0]:
                res = res + 1
                first = points[i][1]
        return res