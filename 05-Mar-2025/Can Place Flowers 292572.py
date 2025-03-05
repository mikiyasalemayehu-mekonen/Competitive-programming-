# Problem: Can Place Flowers - https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        places = 0

        for i in range(len(flowerbed)):
            if flowerbed[i]==0 and i+1<len(flowerbed) and  i-1>=0 :
                if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flowerbed[i] = 1
                    places = places + 1
            elif flowerbed[i]==0 and i+1<len(flowerbed) and  i-1<0 :
                if flowerbed[i+1]==0:
                    flowerbed[i] = 1
                    places = places + 1
            elif flowerbed[i]==0 and i+1>=len(flowerbed) and  i-1>=0 :
                if flowerbed[i-1]==0:
                    flowerbed[i] = 1
                    places = places + 1
            elif flowerbed[i]==0  and len( flowerbed)==1:
                places = places + 1
        return places>=n