# Node Class
class Node:

    # function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as Null


# Linked list class contains a Node object
class LinkedList:

    # Function to initialize HEAD
    def __init__(self):
        self.head = None

    # This function prints contents of LinkedList
    # Starting from HEAD
    def printList(self):
        present_ele = self.head
        while(present_ele):
            print(present_ele.data)
            present_ele = present_ele.next

    # Function to Insert a New Node at beginning
    def push(self, new_data):
        # Allocate the Node & Put in the data
        new_node = Node(new_data)

        # Make next of New Node as Head
        new_node.next = self.head

        # Move the Head to point to New Node
        self.head = new_node

    # Size of LinkedList RECURSIVE Function
    def linkedListSizeRec(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.linkedListSizeRec(node.next)


    # Wrapper function to RECURSIVE function
    def linkedListSize(self):
        return self.linkedListSizeRec(self.head)


if __name__ == "__main__":

    # Start with the empty list
    llist = LinkedList()
    
    llist.push(1)
    llist.push(13)
    llist.push(4)
    llist.push(22)
    llist.push(10)
    llist.push(5)

    #llist.push(20)
    #print("After adding value at HEAD")
    #llist.printList()

    #llist.deleteNodeAt(5)
    #print("After deletion at 5: ")
    print("Nodes are : ")
    llist.printList()

    if llist:
        print(llist)
    else:
        print("No")

    print("Size of linked list is: ", llist.linkedListSize())
