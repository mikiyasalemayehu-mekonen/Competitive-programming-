# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        temp_sum=sum(n for n in nums if n%2==0)
        for value,index in queries:
            current_value=nums[index]
            if nums[index]%2==0:
                temp_sum-=current_value
            nums[index]+=value
            if nums[index]%2==0:
                temp_sum+=nums[index]
            ans.append(temp_sum)
        return ans if ans else [0]