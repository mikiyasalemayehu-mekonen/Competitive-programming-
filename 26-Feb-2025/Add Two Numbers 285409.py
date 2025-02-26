# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()  
        sum_node = dummy 

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            temp = val1 + val2 + carry
            carry = temp // 10  
            sum_node.next = ListNode(temp % 10)
            sum_node = sum_node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next  



    