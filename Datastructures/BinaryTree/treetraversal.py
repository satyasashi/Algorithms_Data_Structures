class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


def printInorder(root):
    if root:
        # first recur on left child.
        printInorder(root.left)

        # then print the data of Node
        print(root.value)

        # now recur on right child.
        printInorder(root.right)


def printPostOrder(root):
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.value)


def printPreOrder(root):
    if root:
        print(root.value)
        printPreOrder(root.left)
        printPreOrder(root.right)


if __name__ == "__main__":
    root = Node(11)
    # test comment
    root.left = Node(6)
    root.right = Node(15)

    root.left.left = Node(3)
    root.left.right = Node(8)

    root.right.left = Node(13)
    root.right.right = Node(17)

    root.left.left.left = Node(1)
    root.left.left.right = Node(5)

    # right subtree
    root.right.left.left = Node(12)
    root.right.left.right = Node(14)

    root.right.right = Node(17)
    root.right.right.right = Node(19)

    print("Inorder traversal of Binary Tree: ")
    printInorder(root)

    print("Post order traversal: ")
    printPostOrder(root)

    print("Preorder traversal: ")
    printPreOrder(root)
