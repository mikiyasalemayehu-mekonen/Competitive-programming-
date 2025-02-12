# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        # """
        def reverse(l:int,r:int,s:list[int]):
            left = l
            right = r-1
            while left<right:
                s[left] , s[right] = s[right] ,s[left]
                left = left+1
                right = right-1

        k = k%len(nums)
        nums.reverse()
        reverse(0,k,nums)
        reverse(k,len(nums),nums)

       
        
        