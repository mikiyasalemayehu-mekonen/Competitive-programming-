# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pairs = {n:-1 for n in nums2}
        mono_stack = [nums2[0]]
        for i in range(1,len(nums2)):
          
            while  mono_stack and mono_stack[-1]<nums2[i] :
                    tem = mono_stack.pop()
                    pairs[tem] = nums2[i]
            
                                                    
            mono_stack.append(nums2[i])

        
        for i in range(len(nums1)):
            nums1[i] = pairs[nums1[i]]
        
        return nums1


                    

        