class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp=[]
        first=0
        second=0
        while first<m and second<n:
            if nums1[first]<nums2[second]:
                temp.append(nums1[first])
                first+=1
            else:
                temp.append(nums2[second])
                second+=1
        temp.extend(nums1[first:m])
        temp.extend(nums2[second:])
        for i in range(m+n):
            nums1[i] = temp[i]
