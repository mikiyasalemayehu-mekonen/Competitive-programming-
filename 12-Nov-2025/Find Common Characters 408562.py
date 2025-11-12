# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = list(words[0])
        for word in words[1:]:
            new_ans = []
            for char in ans:
                if char in word:
                    new_ans.append(char)
                    word = word.replace(char, '', 1)
            ans = new_ans
        
        return ans
