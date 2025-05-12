class CircularQueue:
    def __init__(self, capacity=5):
        self.arr = [0] * capacity
        self.n = capacity
        self.f = -1
        self.r = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add(self, x):
        if self.size == 0:
            self.f = self.r = 0
            self.arr[0] = x
            self.size += 1
        elif self.size == self.n:
            print("Queue is full")
            return
        elif self.r < self.n - 1:
            self.r += 1
            self.arr[self.r] = x
            self.size += 1
        elif self.r == self.n - 1:
            if self.arr[0] == 0:
                self.r = 0
                self.arr[self.r] = x
                self.size += 1

    def remove(self):
        if self.size == 0:
            print("Queue is Empty")
        elif self.f == self.n - 1:
            data = self.arr[self.f]
            self.f = 0
            self.size -= 1
            # print(data)
        else:
            data = self.arr[self.f]
            self.f += 1
            self.size -= 1
            # print(data)

    def peek(self):
        if self.size == 0:
            return -1
        return self.arr[self.f]

    def get_size(self):
        return self.size

    def display(self):
        if self.f <= self.r:
            for i in range(self.f, self.r + 1):
                print(self.arr[i], end=" ")
        else:
            for i in range(self.f, self.n):
                print(self.arr[i], end=" ")
            for i in range(0, self.r + 1):
                print(self.arr[i], end=" ")
        print()


# 🧪 Test the CircularQueue
cq = CircularQueue()
cq.add(10)
cq.add(20)
cq.add(30)
cq.add(40)
cq.remove()
cq.remove()

cq.add(50)
cq.add(60)
cq.add(70)

print("Peek value is:", cq.peek())
print("Queue is Empty?", cq.is_empty())
print("Size of Queue is:", cq.get_size())

cq.display()
