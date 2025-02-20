# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        merged = ListNode()
        merged_head =  merged

        while head1 or head2:
            if(head1 and head2) and head1.val<=head2.val:
                merged.next = head1
                head1 = head1.next
            elif (head1 and head2) and head1.val>head2.val:
                merged.next = head2
                head2= head2.next 
            elif head1:
                merged.next = head1
                head1 = head1.next 
            else:
                merged.next = head2
                head2 = head2.next 
            merged = merged.next



        return merged_head.next

