# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = []
        count=Counter(chars)
        for word in words:
            temp=Counter(word)
            flag = True
            for k, v in temp.items():
                if count[k] < v:
                    flag = False
                    break
            if flag:
                ans.append(word)
        return len("".join(ans))

        