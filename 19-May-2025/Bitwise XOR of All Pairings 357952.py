# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1)%2==0 and len(nums2)%2==0:
            return 0
        elif len(nums1)%2!=0 and len(nums2)%2==0:
            xor = nums2[0]
            for i in range(1,len(nums2)):
                xor = xor^nums2[i]
            return xor
        elif len(nums1)%2==0 and len(nums2)%2!=0:
            xor = nums1[0]
            for i in range(1,len(nums1)):
                xor = xor^nums1[i]
            return xor
        else:
            xor = nums1[0]
            for i in range(1,len(nums1)):
                xor = xor^nums1[i]
            for i in range(len(nums2)):
                xor = xor^nums2[i]
            return xor

