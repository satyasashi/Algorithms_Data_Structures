"""
STACK has only one end. For Entry of element or exit of element.
LIFO (Last In First Out)
"""
from sys import maxsize


def create_stack():
    stack = []
    return stack


def push(stack, value):
    if value:
        stack.append(value)
        print("pushed")
    return stack


def is_empty(stack):
    return len(stack) == 0


def pop(stack):
    if is_empty(stack):
        return str(-maxsize-1)

    return stack.pop()


def peek(stack):
    if is_empty(stack):
        return str(-maxsize-1)

    return stack[len(stack)-1]


stack = create_stack()
push(stack, 5)
push(stack, 4)
push(stack, 8)
push(stack, 1)
push(stack, 9)
push(stack, 2)

peek_ = peek(stack)
print("peek: ", peek_)

popped = pop(stack)
print("Popped: ", popped)
