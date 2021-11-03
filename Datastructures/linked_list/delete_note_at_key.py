class Node:
    """A node has 'data' and 'next' pointer to the next node"""

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    """List of Nodes chained together"""

    def __init__(self) -> None:
        self.head = None

    def push(self, new_data):
        """Make this new node as Head."""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_llist(self):
        """Start from the HEAD and print all the Nodes in the LinkedList"""
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

        return

    def deleteNodeAt(self, key):
        """
        We will find out the presence of the 'Key' and delete that
        from the LinkedList.
        Example:
        Elements: 3 *-> 2 *-> 43 *-> 5 *-> 8 *-> 10

        Target Key: 43
        Output: 3 *-> 2 *-> 5 *-> 8 *-> 10
        """
        # Start from HEAD
        temp = self.head

        # if HEAD itself is the Target
        if temp is not None:
            if temp.data == key:
                # make NEXT of current Head as new HEAD & delete the target Node.
                self.head = temp.next
                temp = None
                return

        prev_node = None
        current_node = temp

        # while the node is not None (reach till end of the list)
        while current_node is not None:
            if current_node.data == key:
                # BASE CASE: Break if we found the Key.
                break

            # Remember previous node and keep track of next node.
            prev_node = current_node
            current_node = current_node.next

        # If we didn't find the Key, then we must just return.
        if current_node is None:
            return

        # Once we found the Key in the list, we link up previous_node with upcoming node.
        prev_node.next = current_node.next

        # Once linking up is done, we save memory by removing the Node from memory.
        # So set it to NONE.
        current_node = None


if __name__ == "__main__":
    # Driver Code
    llist = LinkedList()

    # Add Nodes to the Linkedlist
    llist.push(3)
    llist.push(2)
    llist.push(43)
    llist.push(5)
    llist.push(8)
    llist.push(10)

    # Print original list.
    print("Before the deletion: ")
    llist.print_llist()

    print()

    # Delete at a node at key
    llist.deleteNodeAt(3)
    print("After the deletion: ")
    llist.print_llist()
