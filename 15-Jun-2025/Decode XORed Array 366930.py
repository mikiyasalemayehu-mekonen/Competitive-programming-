# Problem: Decode XORed Array - https://leetcode.com/problems/decode-xored-array/description/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans =[ first]
        for i in range(len(encoded)):
            ans.append(ans[-1]^(encoded[i]))
        return ans


        