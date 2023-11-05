class task4:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.head = self.tail = -1
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = self.tail = 0
        else:
            self.head = (self.head - 1) % self.capacity
        self.queue[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.tail = (self.tail - 1) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.head]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
