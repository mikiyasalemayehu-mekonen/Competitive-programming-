class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        reversed_head = prev
        temp = reversed_head
        temp_prev = None
        for i in range(n - 1):
            if temp.next:
                temp_prev = temp
                temp = temp.next
            else:
                return None
        
        if temp_prev:
            temp_prev.next = temp.next
        else:
            reversed_head = temp.next
        prev1 = None
        current = reversed_head
        while current:
            next_node = current.next
            current.next = prev1
            prev1 = current
            current = next_node
        
        return prev1

