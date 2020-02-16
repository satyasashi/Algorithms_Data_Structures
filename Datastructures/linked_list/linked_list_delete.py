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
    
    # Delete Node At a Position
    def deleteNodeAt(self, position):

        # If linked list is empty
        if self.head == None:
            return

        # store Head Node
        present_ele = self.head

        # If Head needs to be removed
        if position == 0:
            self.head = present_ele.next # decide the next Head
            present_ele = None # Remove the present Head
            return

        # Find Previous node of the Node to be deleted
        # elements are as follows
        # 1    2    3    4    5 --> Nodes
        # 0    1    2    3    4 --> Positions
        for i in range(position -1):
            # Default Position --> 0 or HEAD, Node 1
            print("Position is ", present_ele.data)

            # Make present_element from 1st index as we have Position 0 functionality
            present_ele = present_ele.next # has location of Node before Delete Node
            print("present_ele.next is : ", present_ele.data)
            print("i value in for loop is ", i)
            if present_ele is None:
                break

        # If position is more than number of Nodes
        if present_ele is None:
            return
        if present_ele.next is None:
            return

        # Node present_ele.next is the node to be deleted
        # store pointer to the next of node to be deleted
        print("present_ele outside the for loop is ", present_ele.data)
        next_ = present_ele.next.next
        print("present_ele.next.next is :", next_.data)

        # Unlink the node from linked list
        print("present_ele.next is :", present_ele.next.data)
        present_ele.next = None
        print("After deleting the target, present_ele.next is: ", present_ele.next)

        present_ele.next = next_


    # Delete all Nodes
    def deleteList(self):
        # initialize the current node
        current = self.head

        while current:
            next_  = current.next # move next node

            # delete the current node
            del current.data

            current = next_



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

    print("Deleting Nodes...")
    llist.deleteList()
    print("Successfully Deleted")

    if llist:
        print(llist)
    else:
        print("No")
