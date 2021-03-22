

class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.queue = [None]*k
        self.tail = -1
        self.head = 0
        self.size = 0

                        
    def enQueue(self, value: int) -> bool:
        
        if self.isFull():
            return False

        else:
            self.tail = (self.tail + 1) % self.capacity
            self.queue[self.tail] = value
            self.size = self.size + 1
        
        return True
    
    def deQueue(self) -> bool:
        
        if self.isEmpty():
            return False
        
        else:
            tmp = self.queue[self.head]
            self.head = (self.head + 1) % self.capacity

        self.size = self.size - 1
        return True

        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]       

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]       

    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size == self.capacity


#Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
print(obj.enQueue(2))
print(obj.enQueue(2))
print(obj.enQueue(2))
print(obj.enQueue(2))
