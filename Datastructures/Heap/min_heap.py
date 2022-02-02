from os import curdir
import sys


class MinHeap:
    """Min Heap is a tree datastructure where every element at node is less than
    its Descendants or child nodes. We use Array as Heap"""

    def __init__(self, max_size) -> None:
        self.max_size = max_size
        self.cur_size = 0
        self.heap = [0]*(max_size + 1)
        self.heap[0] = -1 * (sys.maxsize)
        self.root = 1

    def heap_push(self, element):
        """In Heap, we always add a new element towards leftmost element of the tree.
        To maintain the Complete Binary Tree Property. After it's inserted, we
        adjust the elements upwards by Comparing & Swapping."""
        if self.cur_size >= self.max_size:
            return

        self.cur_size += 1
        self.heap[self.cur_size] = element  # inserted at the valid index.
        print(self.heap)
        current = self.cur_size

        # SWAP the elements with Parent until it's in the correct place.
        while self.heap[current] < self.heap[current // 2]:
            self.swap_nodes(current, current//2)
            current = current // 2

    def heap_pop(self):
        """In Heap, we always pop the Root. Pick the right most element in the tree,
        then place in the Root, then adjust/swap the elements."""
        popped = self.heap[self.root]
        # replace root with last node in tree.
        self.heap[self.root] = self.heap[self.cur_size]
        self.heap[self.cur_size] = 0  # set the moved last element to 0.
        self.cur_size -= 1
        # adjust the root element downwards to correct place.
        self.min_heapify(self.root)
        return popped

    def min_heapify(self, i):
        """Heapify in general, is a process of converting a Non Heap Complete Binary Tree
        into a Heap Data Structure.

        Min_Heapify takes single element at a time, and keeps it in correct place.
        When we want to build a Min Heap out of a Complete binary tree, we pass each element
        to this function, to keep that element in correct place, respecting the Min-Heap property.

        Such that, at the end of the iteration, we get a Min Heap Data Structure.
        """

        # if the node is not a leaf node & is greater than any of its children, then swap them.
        # Below condition gives True if the passed index is a Leaf Node. Else False.
        if not (i >= self.cur_size // 2 and i <= self.cur_size):
            # If not a leaf node, then we take the smallest of children
            if (self.heap[2 * i] < self.heap[(2 * i)+1]):
                # now check this smallest should with parent then swap if necessary.
                if self.heap[2*i] < self.heap[i]:
                    self.swap_nodes(2*i, i)
                    # check recursively till it swapped to correct place.
                    self.min_heapify(2*i)
            else:
                if self.heap[2*i + 1] < self.heap[i]:
                    self.swap_nodes(2*i + 1, i)
                    # check recursively till it swapped to correct place.
                    self.min_heapify(2*i + 1)

    def build_heap(self):
        """Building Heap is nothing but HEAPIFY process.
        When a Non Heap, Complete Binary Tree is given, we can Heapify it to convert
        it to either a Min Heap or Max Heap

        Heapify process starts from bottom of the non-leaf node to top.
        """
        for i in range(self.cur_size // 2, 0, -1):
            self.min_heapify(i)

    def swap_nodes(self, node1, node2):
        """Swaps given nodes. Used in Heapify process as well."""
        self.heap[node1], self.heap[node2] = self.heap[node2], self.heap[node1]

    def extract_min(self):
        """Returns what's in the ROOT. Just like peek. No change to heap."""
        return self.heap[self.root]

    def print_heap(self):
        """Prints the whole Heap"""
        for i in range(1, (self.cur_size//2) + 1):
            # start from Index 1 to Last NON-LEAF node.
            print("Parent node is : " + str(self.heap[i]) + " Left child is : " + str(
                self.heap[2 * i]) + " Right child is : " + str(self.heap[(2 * i) + 1]))


# Driver Code
min_heap = MinHeap(10)
min_heap.heap_push(5)
min_heap.heap_push(3)
min_heap.heap_push(17)
min_heap.heap_push(10)
min_heap.heap_push(84)
min_heap.heap_push(19)
min_heap.heap_push(6)
min_heap.heap_push(22)
min_heap.heap_push(9)

min_heap.print_heap()

print("Let's check the heapify process...")
min_heap.build_heap()
min_heap.print_heap()

print("Popping...")
print("Popped: ", min_heap.heap_pop())
print("After popped, elements are: ")
min_heap.print_heap()

print("Extracting Min: ", min_heap.extract_min())
