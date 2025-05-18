# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        max_queue = deque()
        max_queue.append(nums2[0])
        hash_map = {nums1[i]:-1 for i in range(len(nums1))}
        for i  in range(1,len(nums2)):
            tem =[ ]
            while max_queue:  
                if max_queue[0]<nums2[i]:
                    hash_map[max_queue.popleft()] = nums2[i]
                else:
                    tem.append(max_queue.popleft())
            max_queue.extend(tem)

            max_queue.append(nums2[i])


        for i in range(len(nums1)):
            nums1[i] = hash_map[nums1[i]]
        return nums1
        
        