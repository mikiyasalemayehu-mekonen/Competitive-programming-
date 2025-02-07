# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product=defaultdict(list)

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                temp_key = nums[i] * nums[j]
                product[temp_key].append([nums[i], nums[j]])
     
        count=0            
        for key,value in product.items():
            temp = len(value)
            if temp > 1:
                temp=temp*2
                count+= temp*(temp-2)      

        return count

        