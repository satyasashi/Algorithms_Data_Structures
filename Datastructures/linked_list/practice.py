class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def swap(self, x, y):
        prevX = None
        currX = self.head

        while currX is not None and currX.data != x:
            pass

    def push(self, node):
        new_node = Node(node)
        new_node.next = self.head

        self.head = new_node

    def printList(self):
        present_ele = self.head

        while present_ele is not None:
            print(present_ele.data)
            present_ele = present_ele.next

if __name__=="__main__":

    llist = LinkedList()
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)

    print("Original order")
    llist.printList()

    llist.reverse()

    print("Reverse order")
    llist.printList()