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

    def swap(self, x, y):
        prevX = None
        currX = self.head

        # loop through and get the 1st Swap Element and also keep track of Previous element.
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head

        # loop through and get the 2nd Swap element and also keep track of Previous element.
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        # current elements are Swap Elements.
        if currX == None and currY == None:
            return

        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY

        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX

        # temp = currY.next
        # currY.next = prevY
        # prevY.next = currX
        # currX.next = temp

        temp = currY.next
        currY.next = currX.next
        currX.next = temp

    def printList(self):
        present_ele = self.head
        while present_ele is not None:
            print(present_ele.data)
            present_ele = present_ele.next


if __name__ == "__main__":

    llist = LinkedList()

    llist.push(8)
    llist.push(4)
    llist.push(9)
    llist.push(2)
    llist.push(45)
    llist.push(3)
    llist.push(5)

    print("Before Swap: ")
    llist.printList()

    llist.swap(2, 3)
    
    print("After Swap: ")
    llist.printList()
    
