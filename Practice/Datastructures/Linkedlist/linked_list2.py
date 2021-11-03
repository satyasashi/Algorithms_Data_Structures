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


from typing import Counter


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

    def inserAtKey(self, key, new_node):
        """If linkedlist is not empty, traverse the list
        and find the key, if found, place the new node next
        to it"""
        current = self.head
        if not current:
            self.head = new_node

        while current:
            if current.data == key:
                temp = current.next
                current.next = new_node
                new_node.next = temp

                print("New node added after key {}.".format(key))
            elif current.next is None:
                print("Key not found.")

            current = current.next

    def delNodeAtKey(self, key):
        # if head is the key and no next nodes
        if self.head.data == key and self.head.next is None:
            self.head = None

        if self.head.data == key and self.head.next is not None:
            temp = self.head
            self.head = temp.next
            del temp

        # now find the Key in the linked list.
        current_node = self.head
        while current_node is not None:
            if(current_node.data == key):
                break

            prev_node = current_node
            current_node = current_node.next
            print(prev_node.data, current_node.data if current_node else current_node)

        if current_node is None:
            # print("Key doesn't present in Linkedlist")
            return

        # if found remove it
        prev_node.next = current_node.next
        current_node = None
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
    print("Pushed new node at Head.")

    # print all the Nodes.
    llist.printList()

    seventh = Node(10)
    llist.append(seventh)

    print("Appended new node at the end.")
    llist.printList()

    seventh = Node(20)
    llist.inserAtKey(100, seventh)

    llist.printList()

    llist.delNodeAtKey(9)
    print()
    llist.printList()
