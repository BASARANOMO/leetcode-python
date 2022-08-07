class MyCircularQueue:
    def __init__(self, k: int):
        self.front = self.rear = 0
        self.elements = [0] * (k + 1)
        self.capacity = k + 1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.elements[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.elements[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.elements[(self.rear - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        # 1 empty slot left
        return (self.rear + 1) % self.capacity == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
