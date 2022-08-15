class Node:
    __slots__ = "prev", "next", "val"

    def __init__(self, val):
        self.prev = self.next = None
        self.val = val


class MyCircularDeque:
    def __init__(self, k: int):
        self.front = self.rear = None
        self.capacity = k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(value)
        if self.isEmpty():
            self.front = node
            self.rear = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(value)
        if self.isEmpty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            node.prev = self.rear
            self.rear = node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = self.rear.prev
        if self.rear:
            self.rear.next = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.front.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.rear.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


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
