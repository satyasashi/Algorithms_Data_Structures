from faulthandler import is_enabled
import sys


class MaxHeap:
    def __init__(self, max_size) -> None:
        self.max_size = max_size
        self.curr_size = 0
        self.heap = [0]*(max_size+1)
        self.heap[0] = sys.maxsize
        self.root = 1

    def is_leaf(self, indx):
        """Returns True if the element in heap is a leaf. Else False."""
        return indx >= self.curr_size // 2 and indx <= self.curr_size

    def swap_nodes(self, node1, node2):
        """SWAP Parent with Child node."""
        self.heap[node1], self.heap[node2] = self.heap[node2], self.heap[node1]

    def heap_push(self, element):
        """We always push a new element at the left most element end of the tree."""
        # check if the Heap is full, if yes return.
        if self.curr_size >= self.max_size:
            return

        # insert at the end of the tree left-most.
        self.curr_size += 1
        self.heap[self.curr_size] = element

        # Adjust the element upwards.
        # Compare the current element with parent, & swap if necessary.
        current = self.curr_size
        while self.heap[current] > self.heap[current // 2]:
            self.swap_nodes(current, current // 2)
            current = current // 2

    def heap_pop(self):
        """Always pop the Root & take the left most element of the tree
        place in the Root. Now adjust the element downwards. This maintains the
        Heap property."""
        popped = self.heap[self.root]
        # last element of the heap.
        self.heap[self.root] = self.heap[self.curr_size]
        self.heap[self.curr_size] = 0  # set the moved last element to 0.
        self.curr_size -= 1

        # adjust the element downwards.
        self.max_heapify(self.root)
        return popped

    def max_heapify(self, element):
        """Takes an element and adjusts downwards by swapping in the tree."""
        # if index is not a leaf, then do the adjustment process
        if not self.is_leaf(element):
            if self.heap[2 * element] > self.heap[2*element + 1]:
                # if the Left child > Right child, now compare this with parent.
                if self.heap[2*element] > self.heap[element]:
                    self.swap_nodes(2*element, element)
                    # check recursively till it reaches correct position.
                    self.max_heapify(2*element)
            else:
                if self.heap[2*element + 1] > self.heap[element]:
                    self.swap_nodes(2*element+1, element)
                    # check recursively till it reaches correct position.
                    self.max_heapify(2*element+1)

    def build_heap(self):
        """Heapifying the complete binary tree / non-heap tree"""
        for i in range(self.curr_size//2, 0, -1):
            self.max_heapify(i)

    def extract_max(self):
        """Returns what's in the ROOT. Just like peek. No change to heap."""
        return self.heap[self.root]

    def print_heap(self):
        """Print all the Max heap elements"""
        for i in range(self.root, (self.curr_size // 2)+1):
            print("Parent node: {} Left Child: {} Right Child: {}".format(
                self.heap[i], self.heap[2*i], self.heap[2*i + 1]
            ))


# Driver code
max_heap = MaxHeap(10)
max_heap.heap_push(5)
max_heap.heap_push(3)
max_heap.heap_push(17)
max_heap.heap_push(10)
max_heap.heap_push(84)
max_heap.heap_push(19)
max_heap.heap_push(6)
max_heap.heap_push(22)
max_heap.heap_push(9)

print("After insertion, heap is as follows: ")
max_heap.print_heap()

print("Popping ROOT...")
print(max_heap.heap_pop())

print("After popping, Max Heap is as follows:")
max_heap.print_heap()

print("Extracting Max: ", max_heap.extract_max())
