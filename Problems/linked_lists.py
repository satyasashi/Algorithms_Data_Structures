"""
Contains all the problems realted to Linkedlist.
Source: Leetcode / Geeksforgeeks
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def deleteLinkedList(self):
        """This function will delete all the nodes from Linkedlist"""
        current_node = self.head

        while current_node:
            # we need to which node our current_node is pointing to.
            # Once we have that, we can get rid of current_node
            next_node = current_node.next
            del current_node.data
            current_node = next_node

        print("All nodes are deleted.")

    def length_of_linkedlist_iter(self):
        """This function returns the length of Linkedlist using iteration"""
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next

        print("Length of the llist is: ", count)

    def length_of_linkedlist_recur(self, current_node):
        """This function returns the length of linkedlist using Recursion"""
        if current_node:
            return 1 + self.length_of_linkedlist_recur(current_node.next)
        else:
            return 0

    def search_element_in_linkedlist(self, element):
        """This method will return the True if the target element is found else False"""
        if (self.head and self.head.next is None and self.head.data != element) or (self.head is None):
            return False

        current_node = self.head
        while current_node:
            if current_node.data == element:
                return True
            else:
                current_node = current_node.next

        return False

    def nth_node_of_linkedlist(self, position):
        """This will get the Node from linkedlist"""
        current_position = 0
        current_node = self.head
        while current_node:
            if current_position == position:
                return current_node.data
            else:
                current_position += 1
                current_node = current_node.next

        return None

    def nth_node_from_end_of_linkedlist(self, number, size):
        """This will get the Node from end of linkedlist"""
        indx = (size - number)
        count = 0
        current_node = self.head
        while current_node:
            if count == indx:
                return current_node.data
            else:
                current_node = current_node.next
                count += 1

        return False

    def push(self, new_node):
        old_head = self.head
        self.head = new_node
        self.head.next = old_head

    def print_llist(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


if __name__ == "__main__":
    llist = LinkedList()
    elements = list(map(int, input().split(" ")))
    for inx, e in enumerate(elements):
        n = Node(e)
        llist.push(n)

    llist.print_llist()
