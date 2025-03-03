# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_reverse , l2_reverse =None,None
        while l1:
            temp = l1.next
            l1.next = l1_reverse
            l1_reverse = l1
            l1 = temp

        while l2: 
            temp = l2.next
            l2.next = l2_reverse
            l2_reverse = l2
            l2 = temp
        sums = None
        carry = 0

        while l1_reverse or l2_reverse or carry!=0:
            
            temp = ListNode()
            if  l1_reverse and l2_reverse:
                val = l1_reverse.val + l2_reverse.val + carry
                if val<=9:
                    temp.val = val
                    carry = 0
                else:
                    temp.val = val%10
                    carry = val//10
                l1_reverse = l1_reverse.next
                l2_reverse = l2_reverse.next
            elif l1_reverse:
                val = l1_reverse.val + carry
                if val<=9:
                    temp.val = val
                    carry = 0
                else:
                    temp.val = val%10
                    carry = val//10
                l1_reverse = l1_reverse.next
            elif l2_reverse:
                val = l2_reverse.val + carry
                if val<=9:
                    temp.val = val
                    carry = 0
                else:
                    temp.val = val%10
                    carry = val//10
                l2_reverse = l2_reverse.next
            else:
                temp.val = carry
                carry = 0 
            temp.next = sums
            sums = temp


        return sums
        

