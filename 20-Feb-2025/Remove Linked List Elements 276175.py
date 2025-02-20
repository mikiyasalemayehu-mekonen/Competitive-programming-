# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head ==None:
            return head
        dummy = ListNode(None,head)
        temp = dummy
        while temp and temp.next:
            prev = temp
            temp = temp.next
            if temp.val ==val:
                delete = prev.next
                prev.next = temp.next
                delete.next = None
                temp = prev
      
        return dummy.next

        