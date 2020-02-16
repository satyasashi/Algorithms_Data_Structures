"""
Doubly Linked List is similar to Single Linked List, but has ability to go Forward in the list
and also Backward in the list.
                                      +----------------------------------------+        +----------------------------------------+
Which means, a NODE has 3 elements. - | Previous_Pointer | Data | Next_Pointer | -----> | Previous_Pointer | Data | Next_Pointer |
                                      +----------------------------------------+ <----- +----------------------------------------+
"""

class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


class DoublyLinkedList:
    def __init__(self):
        self.head = None


    # Add Node at the end of DLL
    # Traverse throught the DLL and add at the end.
    def append(self, new_data):
        new_node = Node(new_data)

        # This new node is going to be at the end
        # so make it's 'next' as NULL
        new_node.next = None

        # If DLL is empty, make this new_node as Head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        # Go till last from head. Use loop.
        last = self.head

        # Traverse through the DLL
        while (last.next is not None):
            last = last.next

        last.next = new_node
        new_node.prev = last
        return


    def printList(self):
        present_ele = self.head

        while present_ele is not None:
            print(present_ele.data)
            present_ele = present_ele.next

        return

if __name__ == "__main__":
    llist = DoublyLinkedList()

    llist.head = Node(1)

    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    llist.head.next = second
    second.prev = llist.head

    second.next = third
    third.prev = second

    third.next = fourth
    fourth.prev = third

    llist.printList()
    print("Adding 99 at the end...")
    llist.append(99)
    print("Added.")

    llist.printList()

