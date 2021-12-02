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


    def delete_at(self, position):
        present_ele = self.head

        if present_ele == None:
            return

        if position == 0:
            self.head = present_ele.next
            present_ele = None
            return

        for i in range(position - 1):
            present_ele = present_ele.next

            if present_ele is None:
                break

        if present_ele == None:
            print("Present element is None")
            return

        if present_ele.next == None:
            print("Next element is None")
            return