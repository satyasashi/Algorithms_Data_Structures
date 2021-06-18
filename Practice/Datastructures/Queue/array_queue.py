class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None]*capacity
        self.capacity = capacity

    def isFull(self):
        if self.size == self.capacity:
            return

    def isEmpty(self):
        return self.size == 0

    def EnQueue(self, item):
        if self.isFull():
            print("Queue is Full")
            return

        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = item
        self.size += 1
        print("Added new item to Queue")
        print("Self rare ", self.rear)
        print(self.Q)

    def Dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return

        print("{} dequeued from queue".format(self.Q[self.front]))
        self.front = (self.front + 1)
        self.size = self.size - 1

    # Queue function to get FRONT of the queue.
    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")
            return

        print("Front Element in the queue is {}".format(self.Q[self.front]))
        return

    # Queue to get the rear Element.
    def que_rear(self):
        if self.isEmpty():
            print("Queue is Empty")

        print("Element in the Rear is  {}".format(self.Q[self.rear]))
        return


if __name__ == "__main__":
    q = Queue(5)
    q.EnQueue(1)
    q.EnQueue(2)
    q.EnQueue(3)

    q.Dequeue()

    q.que_front()
    q.que_rear()
