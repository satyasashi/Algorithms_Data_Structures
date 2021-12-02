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
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Contains methods for Linkedlist"""

    def __init__(self, node):
        self.head = node

    def node_push(self, node):
        """Pushs a new Node at beginning of Linkedlist"""
        if self.head is None:
            self.head = node

        temp = self.head
        self.head = node
        self.head.next = temp

        return

    def node_append(self, node):
        """Appends at the last of Linkedlist"""
        if self.head is None:
            return

        last_ele = self.head
        while last_ele.next is not None:  # traverse till last node
            last_ele = last_ele.next

        # now add new Node at the end.
        last_ele.next = node

        return

    def delete_note_at_pos(self, position):
        """find the position you want to delete
        Keep track of previous element. now connect previous_node's next
        with current_node's next. Then making Current_node --> None"""
        if self.head is None:
            return

        if position == 1:  # Base Case
            temp = self.head
            self.head = temp.next
            temp = None
            return

        current_node = self.head
        for i in range(position - 1):
            prev_node = current_node
            current_node = current_node.next

        prev_node.next = current_node.next
        current_node = None

        return

    def delete_node(self, key):
        print("Key: ", key)
        print("self.head ", self.head.data)
        """Delete the Key found in the Linkedlist"""
        if self.head.data == key and self.head.next is not None:
            # if head is the key, then make new head and delete this.
            temp = self.head
            self.head = temp.next
            temp = None
            return

        if self.head.data == key:  # Base Case
            # if head is the only node, delete it.
            self.head = None
            return

        current_node = self.head
        while current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        prev_node.next = current_node.next
        current_node = None

        return

    def insert_node_after(self, key, new_node):
        # base case
        # if HEAD is the KEY where after KEY we want to insert new node.
        if self.head.data == key and self.head.next is None:
            self.head.next = new_node
            return

        if self.head.data == key:
            temp = self.head.next
            self.head.next = new_node
            new_node.next = temp
            return

        current_node = self.head

        # Loop from HEAD till you find KEY.
        while current_node:
            prev_node = current_node
            current_node = current_node.next

            if prev_node.data == key:
                # If KEY Found, add 'new_node'.
                temp1 = prev_node.next
                prev_node.next = new_node
                new_node.next = temp1
                return

        return

    def print_linked_list(self):
        present_ele = self.head
        while present_ele:
            print(present_ele.data)
            present_ele = present_ele.next
        print("")

        return


if __name__ == "__main__":
    first_node = Node(1)
    llist = LinkedList(first_node)

    # nodes
    second_node = Node(2)
    third_node = Node(3)
    fourth_node = Node(4)
    fifth_node = Node(5)

    # link em up
    first_node.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node
    fourth_node.next = fifth_node

    # push a new Node at the beginning
    sixth_node = Node(6)
    llist.node_push(sixth_node)

    # llist.print_linked_list()

    # new node at last
    seventh_node = Node(7)
    llist.node_append(seventh_node)

    # llist.print_linked_list()

    llist.delete_note_at_pos(2)

    # llist.print_linked_list()

    llist.delete_node(6)
    llist.print_linked_list()

    # new node insertion after another node.
    eighth_node = Node(8)
    llist.insert_node_after(3, eighth_node)
    llist.print_linked_list()
