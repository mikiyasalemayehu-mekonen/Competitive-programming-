class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp1 = ListNode()
        temp2 = ListNode()
        odd = temp1
        even = temp2

        while head and head.next:
            odd.next = head
            even.next = head.next
            head = head.next.next
            odd = odd.next
            even = even.next
        if head:
            odd.next = head
            odd = odd.next

        odd.next = temp2.next
        even.next = None

        return temp1.next
