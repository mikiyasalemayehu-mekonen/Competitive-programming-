class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracket_pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
        }
        for i in range(len(s)):
            if  s[i] in bracket_pairs:
                stack.append(s[i])
            elif s[i] in bracket_pairs.values():
                if len(stack)==0 or bracket_pairs[stack.pop()]!=s[i]:
                    return False
        return len(stack)==0

        
