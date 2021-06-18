'''
    Five nodes have been created.
    We have references to these three blocks as first,
    second and third

    llist.head        second              third     similarly
        |                |                  |               |
        |                |                  |               | till
    +----+------+   +----+------+      +----+------+   +---+------+
    | 1  | None |   | 2  | None |      |  3 | None |...| 5 | None |
    +----+------+   +----+------+      +----+------+   +---+------+
'''

'''
    Now next of first Node refers to second.  So they
    both are linked. Similarly till end Link them up.

    llist.head        second              third
        |                |                  |
        |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  *-------->| 2  | *--------> |  3 | *-------->
    +----+------+     +----+------+     +----+------+
'''


class Node:
    """Node holds Data and Pointer to next Node"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """LinkedList has a Head"""

    def __init__(self):
        self.head = None

    def printList(self):
        # Print all the nodes starting from Head.
        present_ele = self.head

        while present_ele:
            print(present_ele.data)
            present_ele = present_ele.next

    # Insert New Node After
    # Requires Previous Node information
    def insertAfter(self, prev_node, new_element):
        if prev_node is None:
            print("Previous node must be in the LinkedList")
            return

        new_node = Node(new_element)

        new_node.next = prev_node.next

        prev_node.next = new_node


if __name__ == "__main__":
    '''Make a LinkedList object and assign Node object to it'''
    llist = LinkedList()
    llist.head = Node(1)

    # Declare Nodes
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    # Link them
    llist.head.next = second

    second.next = third

    third.next = fourth

    fourth.next = fifth

    # Print them.
    llist.printList()

    print("After inserting Node")
    llist.insertAfter(second, 10)
    llist.printList()
