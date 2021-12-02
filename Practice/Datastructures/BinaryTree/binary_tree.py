"""
A binary tree consists of at most 2 Nodes.
"""


class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


if __name__ == '__main__':
    node = Node(5)
    print(node.value)

    node.left = Node(4)
    node.right = Node(3)

    node.left.left = Node(2)
    node.left.right = Node(1)

    print(node.left.value)
    print(node.right.value)
    print(node.left.left.value)
    print(node.left.right.value)
    # print(node.right.left.value)
    # print(node.right.right.value)
