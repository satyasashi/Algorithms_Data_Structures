class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    """docstring for LinkedList"""
    def __init__(self):
        self.head = None


    def push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    def deleteNode(self, key):
        # store head node
        temp = self.head

        # If Head holds the Node to be deleted.
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        while (temp is not None):
            if (temp.data == key):
                break

            prev = temp
            temp = temp.next

        if(temp == None):
            return

        # Unlink the node from Linkedlist
        prev.next = temp.next

        temp = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


llist = LinkedList()
llist.push(2)
llist.push(1)
llist.push(6)
llist.push(4)
llist.push(3)


print("Created linked list: ")

llist.printList()

llist.deleteNode(4)

print("Linkedlist after deletion: ")
llist.printList()