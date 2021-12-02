"""
Doubly Linked List is similar to Single Linked List, but has ability to go Forward in the list
and also Backward in the list.
                                        +----------------------------------------+        +----------------------------------------+
Which means, a NODE has 3 elements. -   | Previous_Pointer | Data | Next_Pointer | -----> | Previous_Pointer | Data | Next_Pointer |
                                        +----------------------------------------+ <----- +----------------------------------------+
"""


class Node:
    def __init__(self, prev=None, next=None, data=None):
        self.prev = prev
        self.next = prev
        self.data = data


class LinkedList:
    def __init(self):
        self.head = None

    # Push an element at front of the list.

    def push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            # if former head is not None, then take its Prev and point to new node
            self.head.prev = new_node

        # Move Head pointer to new Node.
        self.head = new_node
