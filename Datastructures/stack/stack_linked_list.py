class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None


    def is_empty(self):
        return True if self.head is None else False


    def push(self, data):
        new_node = StackNode(data)
        print("self.head ", self.head)
        print(new_node.data, new_node.next)

        new_node.next = self.head
        print(new_node.data, new_node.next)
        
        self.head = new_node
        print("self.head ", self.head)
        print("{} pushed to stack".format(data))


    def pop(self):
        if (self.is_empty()):
            return float("-inf")
        temp = self.head
        self.head = self.head.next
        popped = temp.data
        return popped

    def peek(self):
        if self.is_empty():
            return float("-inf")
        return self.head.data


# Driver program to test above class
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("{} popped from stack".format(stack.pop()))
print("Top element is {} ".format(stack.peek()))