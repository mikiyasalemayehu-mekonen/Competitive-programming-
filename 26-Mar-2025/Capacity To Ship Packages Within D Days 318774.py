# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(w):
            run_sum = 0
            count = 0
            for i in range(len(weights)):
                run_sum = run_sum + weights[i]
                if run_sum>w:
                    run_sum = weights[i]
                    count = count + 1
            count = count + 1
            return count<=days
        low = max(weights)
        high = sum(weights)
        result = high
        while low<=high:
            mid = (high + low)//2
            if check(mid):
                result = mid
                high = mid - 1
            else:
                low = mid  + 1 
        return result
        