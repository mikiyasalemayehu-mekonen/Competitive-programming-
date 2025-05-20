# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bin_a = bin(start)[2:]
        bin_b = bin(goal)[2:]
        maxi = max(len(bin_a),len(bin_b))
        bin_a =  bin_a.zfill(maxi)
        bin_b =  bin_a.zfill(maxi)
        cnt = 0
        for i in range(maxi):
            tem =1<<i
            
            if start&tem>0 and goal&tem==0 or start&tem==0 and goal&tem>0:
                cnt = cnt + 1
        return cnt
        