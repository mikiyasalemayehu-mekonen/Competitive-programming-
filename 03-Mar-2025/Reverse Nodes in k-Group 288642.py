# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)  
        group_prev = dummy_node  

        while head:
            upto = self.kth(head, k)
            if not upto: 
                break

            group_next = upto.next  
            prev = group_next  
            head_before_reverse = head 
            while head != group_next:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            group_prev.next = prev
            head_before_reverse.next = group_next 
            group_prev = head_before_reverse  

        return dummy_node.next

    def kth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 1:  
            curr = curr.next
            k -= 1
        return curr
