# Stack is like a STACK OF BOOKS. Last In First Out (LIFO)

# Time Complexity of stack for push(), append(), pop(), is_empty() all are --> O(1)
# as there is no looping used and does only one operation at a time.

# Import 'maxsize' from 'sys' module. Used to get -infinite when Stack is empty.
from sys import maxsize


# Creates stack with initial size 0
def create_stack():
    stack = []
    return stack

# Stack is empty when size is 0
def is_empty(stack):
    return len(stack) == 0 # Returns True or False

# Push an item into the stack at the end/top of stack
def push(stack, item):
    stack.append(item)
    print("Item {}".format(item) + " got pushed")


# Pop an item from the stack at the end/top of stack
def pop(stack):
    if (is_empty(stack)):
        return str(-maxsize-1)

    return stack.pop()

stack = create_stack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
push(stack, str(40))

print(pop(stack)+" popped from stack ")