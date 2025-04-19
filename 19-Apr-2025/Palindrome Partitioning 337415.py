# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]
        result = []
        def backtrack( i,path):
            if  i == len(s):
                result.append(path[:])
                return
            for end in range( i+1,len(s)+1):
                if is_palindrome(s[i:end]):
                    backtrack(end, path + [s[i:end]])

        backtrack(0, [])
        return result