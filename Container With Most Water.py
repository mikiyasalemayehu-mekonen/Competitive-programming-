class Solution:
    def maxArea(self, height: List[int]) -> int:
        max1=0
        last=len(height)-1
        first=0
        while first<last:
            temp=(last-first)*min(height[last],height[first])
            max1=max(temp,max1)
            if height[last]>height[first]:
                first+=1
            else:
                last-=1

        return max1
