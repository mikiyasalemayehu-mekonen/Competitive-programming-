class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        last=math.ceil(math.sqrt(c))
        first=0
        while first<=last:
            temp=(first*first)+(last*last)
            if temp==c:
                return True
            elif temp<c:
                first+=1
            else:
                last-=1
        return False
