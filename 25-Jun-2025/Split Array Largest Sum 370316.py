# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(s):
            run_sum = 0
            count = 1
            for i in range(len(nums)):
                run_sum = run_sum + nums[i]
                if run_sum>s:
                    run_sum = nums[i]
                    count = count + 1
            print(s,count)
            return count<=k
        low = max(nums)
        high = sum(nums)
        result = high
        while low<=high:
            mid = (high + low)//2
        
            if check(mid):
                result = mid
                high = mid - 1
            else:
                low = mid  + 1 
        return result