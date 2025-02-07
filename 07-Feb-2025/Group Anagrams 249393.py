# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        anagram=defaultdict(list)
        for i in range(len(strs)):
            temp="".join(sorted(strs[i]))
            anagram[temp] .append(strs[i])
        for value in anagram.values():
            ans.append(value)
        return ans