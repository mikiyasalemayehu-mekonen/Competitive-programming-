# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        index = 0
        sums = 0  
        while index<k:
            temp =  happiness[index]-index if happiness[index]-index >0 else 0 
            sums = sums + temp
            index = index + 1
        return sums
        