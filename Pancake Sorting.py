class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start=0
            while start<end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
        ans=[]
        for i in range(len(arr)-1,-1,-1):
            max1=i
            for j in range(0,i):
                if arr[max1]<arr[j]:
                    max1=j
            flip(max1)
            flip(i)
            ans.append(max1+1)
            ans.append(i+1)
        return ans

