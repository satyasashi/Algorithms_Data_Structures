class Queue():
	def __init__(self, size):
		self.front = 0
		self.rear = 0
		self.size = size
		self.queue = []

	def enqueue(self, element):
		# check if queue size is reached.
		if len(self.queue) == self.size:
			print("Overflow Error")
			return

		# else add the element to queue
		self.queue = self.queue + [element]
		print("Enqueued the element")
		self.rear = len(self.queue)-1

	def peek(self):
		if len(self.queue) > 0:
			print(self.queue[self.front])
		else:
			print("No elements to Peek at!!")
		return

	def dequeue(self):
		# check if queue is empty.
		if len(self.queue) == 0:
			print("Underflow Error: Queue is empty")
			return

		# else remove the Front element from the queue
		print("Dequeued {}".format(self.queue[self.front]))
		del self.queue[self.front]
		return

if __name__ == "__main__":
	myqueue = Queue(5)

	# enqueuing
	myqueue.enqueue(1)
	myqueue.enqueue(2)
	myqueue.enqueue(3)

	# peeking
	myqueue.peek()

	# dequeuing
	myqueue.dequeue()

	# Overflow
	myqueue.enqueue(10)
	myqueue.enqueue(20)
	myqueue.enqueue(30)
	myqueue.enqueue(40)
	myqueue.enqueue(50)
	myqueue.enqueue(60)

	# Underflow
	myqueue.dequeue()
	myqueue.dequeue()
	myqueue.dequeue()
	myqueue.dequeue()
	myqueue.dequeue()
	myqueue.dequeue()
	myqueue.dequeue()
	myqueue.peek()
