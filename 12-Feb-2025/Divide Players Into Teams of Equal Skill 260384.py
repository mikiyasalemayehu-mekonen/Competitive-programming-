# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill)-1
        temp_product = skill[left]+skill[right]
        ans_product = 0
        while left<right:
            temp = skill[left]+skill[right]
            if temp != temp_product:
                return -1
            ans_product = ans_product +(skill[left]*skill[right])
            left = left+1
            right = right-1


        return ans_product

        