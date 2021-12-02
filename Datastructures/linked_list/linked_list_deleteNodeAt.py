'''
    Five nodes have been created.
    We have references to these three blocks as first,
    second and third

    llist.head        second              third     similarly
        |                |                  |          |
        |                |                  |          | till
    +----+------+     +----+------+     +----+------+   +---+------+
    | 1  | None |     | 2  | None |     |  3 | None |...| 5 | None |
    +----+------+     +----+------+     +----+------+   +---+------+
'''

'''
    Now next of first Node refers to second.  So they
    both are linked. Similarly till end Link them up.

    llist.head        second              third
        |                |                  |
        |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | o--------> |  3 | o-------->
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

    # Delete a Node from LinkedList at given Position
    # Pass a Index Value
    def delete_node_at(self, position):
        if self.head is None:
            return

        present_ele = self.head
        # 1 2 3 4 5
        # 0 1 2 3 4
        if position == 0:
            self.head = present_ele.next
            present_ele = None
            return

        for i in range(position - 1):
            '''We have told what to do if Position == 0
            So we make 0th iteration to points to 1st Node
            for 1th iteration, It points to 2nd Node and so on.'''

            # This goes on till the Position Node is found and makes it, present_ele
            present_ele = present_ele.next

            if present_ele is None:
                break

        if present_ele is None:
            print("present_ele is None")
            return

        if present_ele.next is None:
            print("present_ele.next is None")
            return

        next_ = present_ele.next.next

        present_ele.next = None

        present_ele.next = next_

    # Delete all the nodes from the list
    def delete_all_nodes(self):
        '''
            1. Check if there is head and loop through each Node and take it's next Node reference.
            2. Delete present_element/Node's Data
            3. Make next Node as present_element/Node

        '''
        present_ele = self.head

        if present_ele is None:
            print("Nodes should be in LinkedList")

        while present_ele:
            '''We take next node and only delete (Present_ele.data) not whole (present_ele)
            itself, because we still need its reference for next iteration and to make
            Next Node as Present Node'''

            next_ = present_ele.next

            del present_ele.data

            present_ele = next_


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
    print("After deletion at position 3")
    llist.delete_node_at(0)
    llist.printList()

    print("Deleting all the Nodes...")
    llist.delete_all_nodes()
    print("Done.")
