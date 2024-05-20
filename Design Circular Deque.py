

class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = deque(maxlen=k)
        self.last = 0
        self.max = k

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.max:
            self.queue.appendleft(value)
            self.last += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.max:
            self.queue.append(value)
            self.last += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.queue) > 0:
            self.queue.popleft()
            self.last -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.queue) > 0:
            self.queue.pop()
            self.last -= 1
            return True
        return False

    def getFront(self) -> int:
        if len(self.queue) > 0:
            return self.queue[0]
        return -1

    def getRear(self) -> int:
        if len(self.queue) > 0:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return self.last == self.max


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
