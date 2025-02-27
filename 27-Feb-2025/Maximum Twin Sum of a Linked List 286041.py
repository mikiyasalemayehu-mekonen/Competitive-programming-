# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = ListNode()
        count = 0
        heads_head = head
        while head:
            temp = ListNode(head.val,prev)
            head = head.next
            prev = temp
            count = count + 1
    
        maximum = 0
        for i in range(count//2):
            maximum = max(maximum,heads_head.val+prev.val)
            heads_head = heads_head.next
            prev = prev.next
      
        return maximum
        
        