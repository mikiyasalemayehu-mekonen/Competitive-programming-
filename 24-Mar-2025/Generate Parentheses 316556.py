# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(store, open_count, close_count):
            if len(store) == 2 * n:
                ans.append(store)
                return
            if open_count < n:
                backtrack(store + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(store + ")", open_count, close_count + 1)
        
        backtrack("", 0, 0) 
        return ans


        