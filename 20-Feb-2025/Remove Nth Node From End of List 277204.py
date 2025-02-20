# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return 
        if not head.next:
            return
        temp = head
        slow = head
        fast = head 
        for i in range(n-1):
            fast = fast.next
        prev = ListNode() 
        while fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next
        if slow ==head:
            temp = head.next
            head = temp
        else:

            prev.next = slow.next       
        return head


        