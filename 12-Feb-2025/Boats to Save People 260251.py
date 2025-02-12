# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        left = 0
        right = len(people) -1
        while left<=right:
            if people[right] + people[left] <=limit:
                boats +=1
                left+=1
                right-=1
            
            else:
                boats =  boats+1
                right-=1
           
    

        return boats

        