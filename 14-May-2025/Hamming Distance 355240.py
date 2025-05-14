# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        for i in range(32):
            t = 1<<i
            tem_x = t&x
            tem_y = t&y
            if (tem_x==0 and tem_y!=0) or (tem_x!=0 and tem_y==0):
                cnt = cnt + 1
        return cnt