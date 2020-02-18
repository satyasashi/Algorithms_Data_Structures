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
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal of Binary Tree: ")
    printInorder(root)

    print("Post order traversal: ")
    printPostOrder(root)

    print("Preorder traversal: ")
    printPreOrder(root)
