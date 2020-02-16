'''
    Five nodes have been created.
    We have references to these three blocks as first,
    second and third

    llist.head        second              third     similarly
         |                |                  |          |
         |                |                  |          | till 
    +----+------+     +----+------+     +----+------+   +---+------+
    | 1  | None |     | 2  | None |     |  3 | None |...| 5 | None |
    +----+------+     +----+------+     +----+------+   +---+------+
'''

''' 
    Now next of first Node refers to second.  So they 
    both are linked. Similarly till end Link them up.
  
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  | o--------> |  3 | o--------> 
    +----+------+     +----+------+     +----+------+  
'''


class Node:
    """Node holds Data and Pointer to next Node"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """LinkedList has a Head"""
    def __init__(self):
        self.head = None


    def printList(self):
        # Print all the nodes starting from Head.
        present_ele = self.head

        while present_ele:
            print(present_ele.data)
            present_ele = present_ele.next

    # Delete a Node from LinkedList
    # Pass a KEY
    def delete_node(self, key):
        present_ele = self.head
        # If HEAD is the KEY we need to Delete
        if present_ele is not None:
            if present_ele.data == key:
                # Make next Node as HEAD and kill former Head
                self.head = present_ele.next
                present_ele = None
                return

        # If not in Head, search in the LinkedList
        # Keep track of Previous-Node as we need it's -> .next
        while present_ele is not None:
            if present_ele.data == key:
                break # Break out of the loop
            prev = present_ele # Remember! present element becomes Previous, when we go forward.
            # just like incrementing, we point to next node
            present_ele = present_ele.next

        if (present_ele==None):
            return

        # Unlink the Node to be Deleted
        prev.next = present_ele.next
        present_ele = None



if __name__=="__main__":
    '''Make a LinkedList object and assign Node object to it'''
    llist = LinkedList()
    llist.head = Node(1)

    # Declare Nodes
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    # Link them
    llist.head.next = second

    second.next = third

    third.next = fourth

    fourth.next = fifth

    # Print them.
    llist.printList()
