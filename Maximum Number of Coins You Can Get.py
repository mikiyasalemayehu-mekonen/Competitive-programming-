class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)//3
        temp = piles[n:]
        sum1=0
        for i in range(0,len(temp),2):
            sum1=sum1+temp[i]
        return sum1
