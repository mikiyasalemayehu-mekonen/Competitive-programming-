# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        left = 0
        right = len(s1)-1
        count_s2 = Counter(s2[:len(s1)])
        print(count_s1)
        print(count_s2)      
        while right<len(s2): 
            if count_s1==count_s2:
                return True 
            count_s2[s2[left]] = count_s2[s2[left]] - 1
            left = left +  1 
            right = right + 1
            if right<len(s2):
                count_s2[s2[right]] = count_s2.get(s2[right],0) + 1            
        return False
        