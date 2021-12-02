class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        if self.front is None:
            return

    def EnQueue(self, item):
        temp = Node(item)

        if self.rear is None:
            self.front = self.rear = temp
            return

        self.rear.next = temp
        self.rear = temp

    def DeQueue(self):
        if self.isEmpty():
            return

        temp = self.front
        self.front = temp.next

        if(self.front is None):
            self.rear = None


if __name__ == "__main__":
    q = Queue()
    node1 = Node(2)
    node2 = Node(3)
    node3 = Node(5)
    node4 = Node(6)

    q.EnQueue(node1)
    q.EnQueue(node2)
    q.EnQueue(node3)
    q.EnQueue(node4)

    q.DeQueue()
    q.DeQueue()
    print("Queue Front: ", str(q.front.data))
    print("Queue Rear: ", str(q.rear.data))
