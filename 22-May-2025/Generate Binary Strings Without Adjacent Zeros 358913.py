# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = []

        def backtrack(i, stack):
            if len(stack) == n:
                result.append(stack)
                return

            if not stack or stack[-1] == "1":
                backtrack(i + 1, stack + "0")
                backtrack(i + 1, stack + "1")
            else:
                backtrack(i + 1, stack + "1")

        backtrack(-1, "")
        return result
