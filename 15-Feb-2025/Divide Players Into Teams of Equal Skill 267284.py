# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        product = 0
        right = len(skill)-1
        sums = skill[left] + skill[right]
        while left <len(skill)/2 and right>=len(skill)/2:
            if skill[left] + skill[right] == sums:
                product =product + (skill[left] * skill[right]) 
                left = left+ 1
                right =right - 1
               
            else:
                return -1
        return product 
        