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

    # Push/Add the Node at first
    def push(self, new_element):
        present_ele = self.head
        new_node = Node(new_element)

        if present_ele:
            temp_ele = present_ele
            self.head = new_node
            self.head.next = temp_ele
        else:
            self.head = new_node


if __name__ == "__main__":
    '''Make a LinkedList object and assign Node object to it'''
    llist = LinkedList()
    # llist.head = Node(1)

    # Declare Nodes
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    # Link them
    # llist.head.next = second

    # second.next = third

    # third.next = fourth

    # fourth.next = fifth

    # Print them.
    llist.printList()

    print("Pushed New Node at front")
    llist.push(8)
    llist.printList()
