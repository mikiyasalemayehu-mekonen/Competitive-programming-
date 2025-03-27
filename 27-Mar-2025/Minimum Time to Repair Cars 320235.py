# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(minute):
            total_cars = cars
            for i in range(len(ranks)):
                n = int(sqrt(minute/ranks[i]))
                total_cars = total_cars - n
                if total_cars<=0:
                    break
            return total_cars<=0
        low = 1
        high = min(ranks)*cars*cars
        min_minutes = min(ranks)*cars*cars
        while low<=high:
            mid = (low + high)//2
            if check(mid):
                min_minutes = min(mid,min_minutes )
                high = mid - 1
            else:
                low = mid + 1
        return min_minutes