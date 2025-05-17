# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bin_left = bin(left)[2:]
        bin_right = bin(right)[2:]
        max_len = max(len(bin_left), len(bin_right))
        bin_left = bin_left.zfill(max_len)
        bin_right = bin_right.zfill(max_len)
        common_prefix = ""
        for i in range(max_len):
            if bin_left[i] == bin_right[i]:
                common_prefix += bin_left[i]
            else:
                break
        common_prefix += "0" * (max_len - len(common_prefix))

        return int(common_prefix, 2)

