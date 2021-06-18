"""
Linked List:
1. Push
2. Append
3. Insert After
4. Print Linked List
5. Deleting a given key
6. Deleting a key at given position
7. Length of Linked List
"""


class Node:
    """A single Node holds a Data and pointer to Next node."""

    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    """A linkedlist contains list of Nodes that are linked together"""

    def __init__(self):
        self.head = None

    def push(self, new_node):
        """Push an element at front of the list."""
        if self.head:
            temp = self.head
            self.head = new_node
            self.head.next = temp
        else:
            self.head = new_node

        return

    def append(self, new_node):
        """Add the new node at the end of the Linkedlist"""
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        return

    def printList(self):
        """Start from Head and loop till end of the Linkedlist."""
        if self.head:
            current_node = self.head
            while current_node:
                print(current_node.data)
                current_node = current_node.next

            print()
            return
        else:
            return


if __name__ == "__main__":
    # Create a linkedlist
    llist = Linkedlist()

    # create a list of Nodes.
    llist.head = Node(6)
    second = Node(3)
    third = Node(4)
    fourth = Node(8)
    fifth = Node(2)

    sixth = Node(9)

    # link them up
    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    # print all the Nodes.
    llist.printList()

    llist.push(sixth)

    # print all the Nodes.
    llist.printList()

    seventh = Node(10)
    llist.append(seventh)

    llist.printList()
