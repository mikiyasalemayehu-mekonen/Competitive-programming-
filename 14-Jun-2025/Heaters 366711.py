# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort(reverse=True)
        heaters.sort(reverse=True)
        
        def close_heater(house):
            left, right = 0, len(heaters) - 1
            mini = float("inf")
            
            while left <= right:
                mid = (left + right) // 2
                mini = min(mini, abs(heaters[mid] - house))
                
                if heaters[mid] == house:
                    return mini
                elif heaters[mid] > house:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return mini
        
        ans = 0
        for house in houses:
            ans = max(ans, close_heater(house))
        
        return ans