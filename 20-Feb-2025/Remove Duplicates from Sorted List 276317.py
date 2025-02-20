# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None:
            return 
        values = set()
        values.add(head.val)
        temp = head
        while head and head.next:
            prev = head
            head = head.next
            if head.val in values:
                prev.next = head.next
                head = prev
            values.add(head.val)

        return temp

        