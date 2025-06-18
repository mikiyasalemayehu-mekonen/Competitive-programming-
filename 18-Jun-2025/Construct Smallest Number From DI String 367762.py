# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def is_valid(seq):
            for i in range(len(pattern)):
                if pattern[i] == 'I' and seq[i] >= seq[i + 1]:
                    return False
                if pattern[i] == 'D' and seq[i] <= seq[i + 1]:
                    return False
            return True

        def backtrack(path, used):
            if len(path) == len(pattern) + 1:
                if is_valid(path):
                    return path
                return None
            for digit in range(1, 10):
                if digit not in used:
                    used.add(digit)
                    res = backtrack(path + [digit], used)
                    if res:
                        return res
                    used.remove(digit)
            return None

        result = backtrack([], set())
        return ''.join(map(str, result))
