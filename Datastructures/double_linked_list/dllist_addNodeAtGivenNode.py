"""
Doubly Linked List is similar to Single Linked List, but has ability to go Forward in the list
and also Backward in the list.
                                      +----------------------------------------+        +----------------------------------------+
Which means, a NODE has 3 elements. - | Previous_Pointer | Data | Next_Pointer | -----> | Previous_Pointer | Data | Next_Pointer |
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

    # Given a Node as prev_node, insert
    # a new Node after that prev_node.

    def insertAfter(self, prev_node, new_data):

        # Check if prev_node is Null
        if prev_node is None:
            print("This node doesn't exist in DLL")
            return

        # Pass data to create New Node
        new_node = Node(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node

        new_node.prev = prev_node

        if new_node.next is not None:
            # our new node's next node is brought from previous node's 'next' pointer
            # So if that next node is not None then, tie that node with our new_node in reverse
            new_node.next.prev = new_node
