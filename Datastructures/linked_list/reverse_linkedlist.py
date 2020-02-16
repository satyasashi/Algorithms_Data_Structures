class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        '''
        Initialize three pointers prev as NULL, curr as head and next as NULL.
        Iterate trough the linked list. In loop, do following.
        // Before changing next of current,
        // store next node
        next = curr->next

        // Now change next of current
        // This is where actual reversing happens
        curr->next = prev

        // Move prev and curr one step forward
        prev = curr
        curr = next
        '''
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            # update the Prev. Present Current will be prev in next iteration
            prev = current
            current = next_node
        self.head = prev

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

    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.push(6)

    print("Original Linkedlist")
    llist.printList()

    llist.reverse()

    print("Reversed Linkedlist")
    llist.printList()