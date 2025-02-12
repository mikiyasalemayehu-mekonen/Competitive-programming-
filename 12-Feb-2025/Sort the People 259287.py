# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)-1):
            maximum = i
            for j in range(i+1,len(heights)):
                if heights[j]>heights[maximum]:
                    maximum = j
            heights[i] , heights[maximum] = heights[maximum] , heights[i]
            names[i] , names[maximum] = names[maximum] , names[i]
        return names
        