class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def reverse_list(self):
        """
        Reversing seems a bit complex, but it's really easy.
        All you do is just SWAP the pointers. i.e NEXT --> PREV & PREV ---> NEXT

        Assume you have nodes:  (NULL)<-- A <=====>  B <=====> C <=====> D -->(NULL)
        Here:
            A--> prev = [Null], next = B
            B --> prev = A, next = C
            C --> prev = B, next = D
            D --> prev = C, next = [Null]

        Now we need in reverse :     D <=====> C <====> B <=====> A
        All we need to do SWAP the pointers. NEXT to PREVIOUS and PREVIOUS to NEXT
        Here:
            A --> prev = B, next = Null
            B --> prev = C, next = A
            C --> prev = D, next = B
            D --> prev = [Null], next = C

            when this happened, it is represented as (Null) D <=====> C <====> B <=====> A (Null)

        """

        temp = None
        current = self.head # start from head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev

    def push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node


    def printList(self, node):
        while (node is not None):
            print(node.data)
            node = node.next


dll = DoublyLinkedList()
dll.push(4)
dll.push(12)
dll.push(51)
dll.push(2)
dll.push(1)

print("Nodes are:")
dll.printList(dll.head)

print("Reverse Nodes are:")
dll.reverse_list()
dll.printList(dll.head)
