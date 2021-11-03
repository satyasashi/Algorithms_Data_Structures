from typing import Counter


class Node:
    """
    A node has two things. Data & Pointer to the next node
    """

    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None

    def __repr__(self) -> str:
        return "<Node data: {}>".format(self.data)


class LinkedList:
    """
    Singly linked list
    """

    def __init__(self) -> None:
        self.head = None

    def __repr__(self) -> str:
        """
        Returns a string representation of the list
        Takes O(n) time.
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head {}]".format(current.data))
            elif current.next_node is None:
                nodes.append("[Tail: {}]".format(current.data))
            else:
                nodes.append("[{}]".format(current.data))

            current = current.next_node
        return "-> ".join(nodes)

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time.
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, new_data):
        """
        Adds a new node containing data at the head of the list.
        Takes O(1) time. (Best Case Scenario)
        """
        new_node = Node(new_data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the KEY
        Returns the 'node' or None if not found.

        Takes: O(n) time.
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new node containing data at index position
        Insertion takes O(1) time but finding the node at the 
        insertion point takes O(n) time.

        Takes Overall O(n) time.
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1
            prev = current
            next_node = current.next

            prev.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes the node containing the data that matches the KEY.
        Returns the Node or None if doesn't exist.

        Takes O(n) time.
        """
        current = self.head
        prev = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node

            elif current.data == key:
                found = True
                prev.next_node = current.next_node
            else:
                prev = current
                current = current.next_node
        return current
