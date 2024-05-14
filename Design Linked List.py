class MyLinkedList:
    def __init__(self):
        self.val = None
        self.next = None
        
    def get(self, index: int) -> int:
        dummy = self.next
        temp = 0
        while dummy:
            if temp == index:
                return dummy.val
            dummy = dummy.next
            temp += 1
        return -1

    def addAtHead(self, val: int) -> None:
        
        dummy = self.next
        new = MyLinkedList()
        new.val = val
        new.next = dummy
        self.next = new

    def addAtTail(self, val: int) -> None:
        dummy = self
        new = MyLinkedList()
        new.val = val
        while dummy.next:
            dummy = dummy.next
        dummy.next = new
    def addAtIndex(self, index: int, val: int) -> None:
        dummy = self
        for i in range(index):
            if not dummy.next:
                return
            dummy = dummy.next
        new = MyLinkedList()
        new.val = val
        new.next = dummy.next
        dummy.next = new

    def deleteAtIndex(self, index: int) -> None:
        dummy = self
        for i in range(index):
            if not dummy.next:
                break
            dummy = dummy.next
        if dummy.next:
            dummy.next = dummy.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
