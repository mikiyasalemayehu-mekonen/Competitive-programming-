# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        new_head = None
        current = head
        while current:
            new_node = ListNode(current.val) 
            new_node.next = new_head  
            new_head = new_node  
            current = current.next
        while new_head and head:
            if new_head.val != head.val:
                return False
            new_head = new_head.next 
            head = head.next
        return True

        

        # while head and head.next :
        #     temp = head.next.next
        #     temp2 = head.next
        #     head.next = temp
        #     temp2.next = head
        #     head = temp2
        #     print(head)
    
          

        
        