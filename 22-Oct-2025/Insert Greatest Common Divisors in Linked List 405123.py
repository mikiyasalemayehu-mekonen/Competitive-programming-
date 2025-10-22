# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp:

            if temp.next:
                node = temp.next
                g = gcd(temp.val,node.val)
                n = ListNode(g)
                temp.next = n
                n.next = node
                temp = node
            else:
                break

        return head