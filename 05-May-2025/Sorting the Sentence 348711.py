# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        arr=[i[-1]+i[:-1] for i in s.split()]
        arr.sort()
        ans=""
        for i in arr:
            ans+=i[1:]+" "
        return ans[:-1]
        