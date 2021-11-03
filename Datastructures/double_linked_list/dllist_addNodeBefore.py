class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insertNodeBefore(self, reference_node, new_data):
        """Takes in a `reference_node` before which we need
        to place a new_node.

        Else we take the `reference_node` and change the
        pointers accordingly.

        Possible places we might Insert:
        1. Inserting in between any 2 Nodes in the list.
        2. Inserting before the HEAD.
        """

        new_node = Node(new_data)
        new_node.prev = reference_node.prev
        new_node.next = reference_node

        if reference_node.prev is not None:
            # if we are placing new_node in between any 2 nodes.
            reference_node.prev.next = new_node
        else:
            # else if we are placing new_node at front of HEAD,
            # make this new_node as HEAD.
            self.head = new_node

        # finishing up with the connections from reference_node to new_node
        # before it.
        reference_node.prev = new_node

    def printList(self, node):
        print("Doubly Linked List:")
        last = None

        print("Forward Traversal: ")
        while node is not None:
            print(node.data, end=" ")
            last = node
            node = node.next

        print("")

        print("Reverse Traversal: ")
        while last is not None:
            print(last.data, end=" ")
            last = last.prev


if __name__ == "__main__":
    dllist = DoublyLinkedList()
    dllist.head = Node(3)
    second = Node(4)
    third = Node(5)
    fourth = Node(1)

    dllist.head.next = second
    second.prev = dllist.head
    second.next = third
    third.prev = second
    third.next = fourth
    fourth.prev = third

    print("Before:")
    dllist.printList(dllist.head)

    dllist.insertNodeBefore(fourth, 2)

    print("After: ")
    dllist.printList(dllist.head)
