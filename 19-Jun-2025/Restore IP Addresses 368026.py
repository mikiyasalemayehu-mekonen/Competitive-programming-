# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(ip):
            return len(ip) == 1 or (ip[0] != '0' and 0 <= int(ip) <= 255)

        result = []

        def backtrack(i, path):
            if len(path) == 4:
                if i == len(s):
                    result.append(".".join(path))
                return
            for j in range(i + 1, min(i + 4, len(s) + 1)):
                temp = s[i:j]
                if is_valid(temp):
                    path.append(temp)
                    backtrack(j, path)
                    path.pop()

        backtrack(0, [])
        return result
