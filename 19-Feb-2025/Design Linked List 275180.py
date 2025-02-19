# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head
        i = 0
        while temp and i<index:
            temp = temp.next
            i = i + 1
        return temp.val if temp else -1
        

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)

    def addAtTail(self, val: int) -> None:
        temp = Node(val,None)
        if self.head==None:
            self.head = temp
            return 
        temp_node = self.head
        while temp_node.next:
            temp_node = temp_node.next
        temp_node.next = temp
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self. addAtHead(val)
            return
        prev = self.head
        for i in range(index - 1):
            if not prev:
                return 
            prev = prev.next
        if prev:
            new_node = Node(val, prev.next)
            prev.next = new_node
        
    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        prev = self.head
        for i in range(index - 1):
            if not prev.next:
                return
            prev = prev.next
        if prev.next:
            prev.next = prev.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)