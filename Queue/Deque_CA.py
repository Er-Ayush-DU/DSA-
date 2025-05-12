class CircularDeque:
    def __init__(self, capacity=5):
        self.n = capacity
        self.arr = [None] * self.n
        self.front = -1
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.n

    def insert_front(self, x):
        if self.is_full():
            print("Deque is full")
            return

        if self.is_empty():
            self.front = self.rear = 0
        elif self.front == 0:
            self.front = self.n - 1
        else:
            self.front -= 1

        self.arr[self.front] = x
        self.size += 1

    def insert_rear(self, x):
        if self.is_full():
            print("Deque is full")
            return

        if self.is_empty():
            self.front = self.rear = 0
        elif self.rear == self.n - 1:
            self.rear = 0
        else:
            self.rear += 1

        self.arr[self.rear] = x
        self.size += 1

    def delete_front(self):
        if self.is_empty():
            print("Deque is empty")
            return

        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.n - 1:
            self.front = 0
        else:
            self.front += 1

        self.size -= 1

    def delete_rear(self):
        if self.is_empty():
            print("Deque is empty")
            return

        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.rear == 0:
            self.rear = self.n - 1
        else:
            self.rear -= 1

        self.size -= 1

    def get_front(self):
        if self.is_empty():
            return -1
        return self.arr[self.front]

    def get_rear(self):
        if self.is_empty():
            return -1
        return self.arr[self.rear]

    def display(self):
        if self.is_empty():
            print("Deque is empty")
            return

        i = self.front
        while True:
            print(self.arr[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.n
        print()


# Test the deque
dq = CircularDeque()

dq.insert_rear(10)
dq.insert_rear(20)
dq.insert_front(5)
dq.insert_front(2)
dq.display()  # 2 5 10 20

dq.delete_rear()
dq.delete_front()
dq.display()  # 5 10

print("Front:", dq.get_front())  # 5
print("Rear:", dq.get_rear())    # 10
print("Size:", dq.size)
print("Empty:", dq.is_empty())
