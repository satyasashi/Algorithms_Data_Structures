"""
A Heap is a special Tree-based data structure in which the tree is a complete binary tree. Generally, 
Heaps can be of two types:

1. Max-Heap: 

In a Max-Heap the key present at the root node must be greatest among the keys present at all of it’s children. 
The same property must be recursively true for all sub-trees in that Binary Tree.


Examples of Min Heap:

            10                      10
			/  \\               /       \\  
		20        100          15         30  
		/                    /  \\       /  \\
    30                     40    50    100   40


2. Min-Heap: 

In a Min-Heap the key present at the root node must be minimum among the keys present at all of it’s children. 
The same property must be recursively true for all sub-trees in that Binary Tree.


"""
from heapq import heappush, heappop, heapify


class MinHeap:
    """We represent a Binary Heap as an Array"""

    def __init__(self):
        # let's call this array as 'heap'
        self.heap = []

    def parent(self, i):
        # this formula gives the Parent of the current node at index 'i'
        # A tree having 4 Elements/Nodes in it, if index 'i' is 4,
        # then Parent node is at (4-1)/2 --> Floor value. Which is '1'.
        # therefore, Parent of Node 30 is --> 20.
        return (i-1)//2

    def insert_key(self, k):
        # This will add the new Key at the End of the tree.
        # If the value violates the Min Heap property, then
        # we traverse Upwards to place this in correct position.
        heappush(self.heap, k)

    def decrease_key(self, indx, new_val):
        """This is where we specify which index element need to be
        Decreased and Swapped. 
        If we want to Delete a key:
        - We replace the original value with Negative Infinity
        - Then traverse this upwards
        Else:
        - We replace with the value we wanted.
        """
        self.heap[indx] = new_val

        # As long as the new value inserted is LESS than Parent, Keep Swapping.
        while (indx != 0 and self.heap[self.parent(indx)] > self.heap[indx]):
            # we now want to swap this reduced value to the correct place.
            print("Index is {}. Parent Node is {}. Current Node is {}".format(
                indx, self.heap[self.parent(indx)], self.heap[indx])
            )
            self.heap[indx], self.heap[self.parent(indx)] = \
                self.heap[self.parent(indx)], self.heap[indx]

    def extract_minimum(self):
        """
        This will Remove/Pops the Minimum element from the Binary Heap.
        We shall use the 'heapq' library for that.
        """
        return heappop(self.heap)

    def delete_key(self, indx):
        """
        This will first reduce the Target indx value to Negative Infinity,
        swaps this negative value to the top of the tree to maintain Min-Heap
        property. Then extracts the Minimum element from the existing tree and
        returns it.
        """
        self.decrease_key(indx, float("-inf"))
        self.extract_minimum()

    def get_minimum(self):
        """As we always know that 0th index is the Minimum Element"""
        return self.heap[0]


if __name__ == "__main__":
    # Driver code to use the Min-Heap
    """
                    10
                    /  	\\
            40   		20
            /  \\		/	\\
    45  	50		70	  65
    """
    heap_obj = MinHeap()
    heap_obj.insert_key(3)
    heap_obj.insert_key(2)
    heap_obj.insert_key(1)
    heap_obj.insert_key(15)
    heap_obj.insert_key(5)
    heap_obj.insert_key(4)
    heap_obj.insert_key(45)

    print("Delete the Minimum: ", heap_obj.extract_minimum())
    print("Get the Minimum element: ", heap_obj.get_minimum())

    heap_obj.decrease_key(2, 1)

    print("Get the Minimum element: ", heap_obj.get_minimum())
    print("elements are: ", heap_obj.heap)
