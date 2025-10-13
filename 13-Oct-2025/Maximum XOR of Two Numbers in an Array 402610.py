# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        maxi = max(nums)
        binary = bin(maxi)[2:]
        n = len(binary)
        xor_num = [bin(num)[2:].zfill(n) for num in nums]
     
        trie = {}
        for word in xor_num:
            current = trie  
            for ch in word:
                if ch not in current:
                    current[ch] = {}
                current = current[ch]
        xor_max = []
        for word in xor_num:
            current = trie  
            tem = []
            for ch in word:
                ch = "0" if ch=="1" else "1"
                if ch not in current:
                    ch = "0" if ch=="1" else "1"
                tem.append(ch)
                current = current[ch]
            tem = int("".join(tem),2)
            xor_max.append(tem)
        res = 0
        for n1,n2 in zip(xor_max,nums):
            res = max(res,n1^n2)
        return res
