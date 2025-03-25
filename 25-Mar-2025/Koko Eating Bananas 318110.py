# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def check(self,piles,val,h):
        count = 0
        for i in range(len(piles)):
            count = count + math.ceil(piles[i]/val)
        return count<=h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = max(piles)
        low = 1
        high = max(piles)
        while low<=high:
            mid = (high + low)//2
            if self.check(piles,mid,h):
                result =  min(mid,result)
                high = mid - 1
            else:
                low = mid + 1
        return result
