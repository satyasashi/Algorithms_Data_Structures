# Simple python program for traversal of a Linked List

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

    # Add a Node after a given Previous Node
    def insertAfter(self, prev_node, new_data):
        
        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must be in LinkedList")
            return

        # 2. Create New Node & Put in the data
        new_node = Node(new_data)

        # 3. Make next of New Node as next of Prev_node
        new_node.next = prev_node.next

        # 4. Make next of Prev_node as New Node
        prev_node.next = new_node


    # Add Node at the end
    def append(self, new_data):
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the LinkedList is empty, then make the new node
        # as Head
        if self.head is None:
            self.head = new_node
            return
        
        # 5. else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node


    # Delete a Node
    def deleteNode(self, key):
        # store head Node
        present_ele = self.head
        print('present_ele is: ', present_ele)

        # if Head Node itself holds the key to be Deleted
        # Take Head Node's next node as Head and delete this Head
        if(present_ele is not None): # if present_ele is None then LList is empty.
            if (present_ele.data == key):
                self.head = present_ele.next
                present_ele = None
                return

        # Search for the Key to be deleted, Keep track of 
        # previous Node as we need to change 'prev.next'
        while (present_ele is not None):
            if present_ele.data == key:
                break
            prev = present_ele
            present_ele = present_ele.next

        # If key was not present in Linked list
        if(present_ele==None):
            return
        
        # Unlink the node from linked list
        prev.next = present_ele.next

        present_ele = None


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

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    seventh = Node(7)
    
    llist.head.next = second # Link first node with second

    

    second.next = third # Link second node with third
    
    third.next = fourth # Link third node with Fourth

    fourth.next = fifth # Link fourth node with Fifth

    fifth.next = sixth # Link fifth node with Sixth

    sixth.next = seventh # Link sixth node with Seventh

    llist.printList()
    
    #llist.push(20)
    #print("After adding value at HEAD")
    #llist.printList()

    #print("Add a node after a Given Node")
    #llist.insertAfter(llist.head, 70)
    #llist.printList()

    #print("Add a Node at the END")
    #llist.append(90)
    #llist.printList()
    
    llist.deleteNodeAt(5)
    print("After deletion at 5: ")
    llist.printList()
