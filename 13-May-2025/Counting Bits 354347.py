# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]
        ans = [0]
        for i in range(1,n+1):
            tem = i 
            cnt = 0
            while tem!=0:
                rem = tem%2
                if rem==1:
                    cnt = cnt + 1
                tem = tem//2
            ans.append(cnt)
        return ans
        
        