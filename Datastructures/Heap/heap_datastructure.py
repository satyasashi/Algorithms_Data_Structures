"""
A Heap is a special Tree-based data structure in which the tree is a complete binary tree. Generally, 
Heaps can be of two types:

1. Max-Heap: 

In a Max-Heap the key present at the root node must be greatest among the keys present at all of it’s children. 
The same property must be recursively true for all sub-trees in that Binary Tree.


Examples of Min Heap:

            10                      10
         /      \\               /       \\  
       20        100          15         30  
      /                      /  \\       /  \\
    30                     40    50    100   40


2. Min-Heap: 

In a Min-Heap the key present at the root node must be minimum among the keys present at all of it’s children. 
The same property must be recursively true for all sub-trees in that Binary Tree.


"""
from heapq import heappush, heappop, heapify


class MinHeap:
	def __init__(self):
		self.heap = []

	
	def parent(self, i):
		return (i-1)/2


	def insertKey(self, k):
		heappush(self.heap, k)


	