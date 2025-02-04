# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        sample_count = count[s[0]]
        for key,value in count.items():
            if count[key]!=sample_count:
                return False
        return True


        