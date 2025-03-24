# Problem: The k-th Lexicographical String of All Happy Strings of Length n - https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        words =['a', 'b', 'c']
        def backtrack(store,n):
            nonlocal words
            if len(store)==n:
                ans.append(store[:])
                return
            for i in range(3):
                if words[i] not in store[-1:]:
                    store.append(words[i])
                    backtrack(store,n)
                    store.pop()
        backtrack([],n)
        return "".join(ans[k-1]) if k-1<len(ans) else ""