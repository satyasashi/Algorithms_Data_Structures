class Queue():
	def __init__(self, size):
		self.front = 0
		self.rear = 0
		self.queue = []
		self.size = size

	def enqueue(self, element):
		# check if queue size is fulfilled
		if len(self.queue) == self.size:
			print("Queue Overflow")
			return
		# else append the element to queue.
		self.queue.append(element)
		print("Enqueued Element")

		# if elements present, make tail to point
		# to last element in queue
		self.rear = len(self.queue)-1 if len(self.queue) > 1 else 0
		return

	def dequeue(self):
		# check if Queue is already empty. If yes, throw Underflow Error
		if len(self.queue) == 0:
			print("UnderflowError: No elements in your queue")
			return

		# else Dequeue element from Queue
		print("Dequeued {}".format(self.queue[self.front]))
		self.queue.pop(self.queue.index(self.queue[self.front]))
		self.rear = len(self.queue)-1 if len(self.queue) > 1 else 0
		print(self.queue)
		return

	def peek(self):
		# peek first element in the queue
		print(self.queue[self.front])
		return

if __name__ == "__main__":
	myqueue = Queue(5)
	myqueue.enqueue(1)
	myqueue.enqueue(2)
	myqueue.peek()

	myqueue.dequeue()
	myqueue.peek()
	myqueue.dequeue()
	myqueue.dequeue()
	myqueue.dequeue()
	myqueue.dequeue()
	myqueue.dequeue()
	myqueue.dequeue()
	myqueue.dequeue()
