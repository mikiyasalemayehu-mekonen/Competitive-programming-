# Problem: Remove Nodes From Linked List - https://leetcode.com/problems/remove-nodes-from-linked-list/description/?envType=problem-list-v2&envId=recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
        prev = None
        while head:
            tem = head.next
            head.next = prev
            prev = head
            head = tem

        new_head = prev
        max_val = prev.val
        cur = prev
        while cur and cur.next:
            if cur.next.val < max_val:
                cur.next = cur.next.next
            else:
                cur = cur.next
                max_val = cur.val
        prev = None
        while new_head:
            tem = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = tem

        return prev


        