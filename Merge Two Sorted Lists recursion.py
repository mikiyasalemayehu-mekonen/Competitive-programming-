
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        def sort(list1,list2):
            if  not list1:
                return list2
            if  not list2:
                return list1 
            if list1.val < list2.val:
                list1.next=sort(list1.next,list2)
                return list1
            else :
                list2.next=sort(list1,list2.next)
                return list2
        curr.next=sort(list1,list2)
        return dummy.next
        
