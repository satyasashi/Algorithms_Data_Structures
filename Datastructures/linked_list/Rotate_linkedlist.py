'''
Given a singly linked list, rotate the linked list counter-clockwise by k nodes.
Where k is a given positive integer. For example, if the given linked list is 10->20->30->40->50->60 and 
k is 4, the list should be modified to 50->60->10->20->30->40. Assume that k is smaller than the count of 
nodes in linked list.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, node):
        new_node = Node(node)

        new_node.next = self.head

        self.head = new_node

    def printList(self):
        present_ele = self.head

        while present_ele != None:
            print(present_ele.data)
            present_ele = present_ele.next

    def rotate(self, key):
        if key == 0:
            return

        count = 1
        current = self.head

        while(count < key and current is not None):
            current = current.next
            count += 1

        if current is None:
            return

        kthNode = current

        while (current.next is not None):
            current = current.next

        current.next = self.head

        self.head = kthNode.next

        kthNode.next = None

if __name__ == "__main__":

    llist = LinkedList()

    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)

    llist.printList()

    llist.rotate(4)
    print("After Rotating at key 4: ")
    llist.printList()