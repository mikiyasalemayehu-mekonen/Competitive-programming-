# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        maps = { }
        for nm in arr:
            
            maps[nm%k] = maps.get(nm%k,0) + 1
        for rem in maps:
            tem = maps[rem]
            if rem==0 and tem%2!=0:
                return False
            if rem==0:
                continue
            if k-rem not in maps or maps[rem]!=maps[k-rem]:
               
             
                return False
        return True
        