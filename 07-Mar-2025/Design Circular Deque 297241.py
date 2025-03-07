# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/



class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = deque(maxlen=k)
        self.size = 0
        self.max = k

    def insertFront(self, value: int) -> bool:
        if self.size < self.max:
            self.queue.appendleft(value)
            self.size+= 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.size < self.max:
            self.queue.append(value)
            self.size+= 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.size > 0:
            self.queue.popleft()
            self.size-= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.size > 0:
            self.queue.pop()
            self.size-= 1
            return True
        return False

    def getFront(self) -> int:
        if self.size > 0:
            return self.queue[0]
        return -1

    def getRear(self) -> int:
        if self.size > 0:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size ==self.max


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()