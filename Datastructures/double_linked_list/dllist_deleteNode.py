# import the Garbage Collector
import gc

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # head_ref--> pointer to head node pointer
    # dele --> pointer to node to be deleted
    def deleteNode(self, dele):
        # Best Case
        if self.head is None or dele is None:
            return

        # If node to be deleted is Head Node,
        # Then make Next element as New Head
        if self.head == dele:
            self.head = dele.next

        # change next only if Node to be deleted is NOT
        # the last node.
        # ex: take NEXT Node's Previous and connect to PREVIOUS Node
        if dele.next is not None:
            dele.next.prev = dele.prev

        # If deleting-node's prev is not None, take that prev's next and point to
        # Next Node.
        if dele.prev is not None:
            dele.prev.next = dele.next

        # Finally, free the memory occupied by 'dele'
        # call python garbage collector
        gc.collect()


    # Given reference to self.head of list, and passing
    # New Node at the front of the list Makin this new head.
    def push(self, new_data):
        # 1. Allocates node
        # 2. Put the data in it.
        new_node = Node(new_data)

        # 3. Point next of this new head to old head
        new_node.next = self.head

        # 4. Change prev of old_head node to new_head
        if self.head is not None:
            self.head.prev = new_node

        # 5 Move the head to point to New Head
        self.head = new_node


    # print the list of nodes, starting from given nodes
    def printList(self, node):
        while(node is not None):
            print(node.data)
            node = node.next


dll = DoublyLinkedList()

# Push each element at the first of list.
dll.push(2)
dll.push(4)
dll.push(8)
dll.push(10)
dll.push(12)

# Print all the Nodes in the list.
print("All the nodes: ")
dll.printList(dll.head)
print()

print("Deleting the Head...")
# Delete nodes from doubly linked list
dll.deleteNode(dll.head)
print("Deleted")
print("Now the remaining nodes are:")
dll.printList(dll.head)