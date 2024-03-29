class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.cap = k
        self.q = [0] * k
        self.front = self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.rear == -1:
            self.rear = self.front = 0
        else:
            self.rear = (self.rear + 1) % self.cap
        self.q[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.cap
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.q[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap      


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()