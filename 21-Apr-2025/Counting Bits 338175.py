# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]
        ans = [0,1]
        for i in range(2,n+1):
            cnt = 0
            while i>0:
                temp = i%2
                i = i//2

                if temp==1:
                    cnt = cnt + 1
            ans.append(cnt)
        return ans


        