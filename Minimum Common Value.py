class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        index1=0
        index2=0
        while index1<len(nums1) and index2<len(nums2):
            if nums1[index1]==nums2[index2]:
                return nums1[index1]
            elif nums1[index1]<nums2[index2]:
                index1+=1
            else :
                index2+=1
                
        return -1
