class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, node):
        self.head = node

    def push(self, data):
        if self.head is not None:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next

            curr_node.next = StackNode(data)
        else:
            self.head = StackNode(data)

        return

    def pop(self):
        if self.head is not None:
            curr_node = self.head
            temp_node = None
            while curr_node.next is not None:
                temp_node = curr_node
                curr_node = curr_node.next

            temp_node.next = None
            return curr_node.data
        else:
            return

    def peek(self):
        if self.head is not None:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next

            return curr_node.data
        else:
            return None

    def is_empty(self):
        if self.head is not None:
            return False
        else:
            return True

    def llist_loop(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next


if __name__ == "__main__":
    stack_node = StackNode(5)
    stack = Stack(stack_node)

    # new nodes
    stack_node1 = StackNode(2)
    stack_node2 = StackNode(8)
    stack_node3 = StackNode(1)
    stack_node4 = StackNode(3)
    stack_node5 = StackNode(0)

    stack_node.next = stack_node1
    stack_node1.next = stack_node2
    stack_node2.next = stack_node3
    stack_node3.next = stack_node4
    stack_node4.next = stack_node5

    # print(stack.is_empty())

    stack.push(7)

    # print(stack.peek())
    #
    # print(stack.pop())
    #
    print(stack.peek())

    stack.push(99)

    print(stack.peek())
