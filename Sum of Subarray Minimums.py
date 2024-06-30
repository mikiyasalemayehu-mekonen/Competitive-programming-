class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        res = 0
        stack = []
        
        for i,n in enumerate(arr):
            while stack and stack[-1][1]>arr[i]:
                j,val=stack.pop()
                left=j-stack[-1][0] if stack else j+1
                right=i-j
                res=(res+(val*left*right))%mod
            stack.append([i,n])
        for i in range(len(stack)):
            j,n=stack[i]
            left=j-stack[i-1][0] if i>0 else j+1
            right=len(arr)-j
            res=(res+(n*left*right))%mod

        return res 
