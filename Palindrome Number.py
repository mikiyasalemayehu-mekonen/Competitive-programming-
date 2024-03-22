class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >=0:
            reverse=0
            temp=x
            while temp>0:
                rem=temp%10
                reverse=reverse*10+rem
                temp=temp//10
            if(x==reverse):
                return True
            else:
                return False
        else:
            return False
