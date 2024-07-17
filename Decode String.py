class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s: str, i: int) -> (str, int):
            result = ""
            num = 0

            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] == '[':
                    substr, i = decode(s, i + 1)
                    result += num * substr
                    num = 0
                elif s[i] == ']':
                    return result, i
                else:
                    result += s[i]
                i += 1

            return result, i

        decoded_string, _ = decode(s, 0)
        return decoded_string
        
