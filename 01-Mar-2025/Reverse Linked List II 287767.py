# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]: 
        if not head or left == right:
            return head
        dummy = ListNode()
        dummy.next = head
        prev, curr = dummy, head
        for i in range(left-1):
            prev = curr
            curr = curr.next
        prev.next = None
        
        rev = None
        rev_head = rev
        for i in range(right-left+1):
            loc = curr.next
            curr.next = rev
            rev = curr
            curr = loc
        
        prev.next = rev
        while prev.next:
            prev = prev.next
        prev.next = curr


        return dummy.next


        