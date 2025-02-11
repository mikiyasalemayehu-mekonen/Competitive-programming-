# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        count = dict(sorted(count.items(),key=lambda item:item[1],reverse=True))
        return "".join([key*val for key,val in count.items()])

        