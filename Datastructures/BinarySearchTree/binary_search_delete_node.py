from binaryInsertionOfKey import BinarySearchTree, Node


class DeleteNode(BinarySearchTree):
    """Deletes a specified key from the Binary Tree"""

    def __init__(self) -> None:
        super().__init__()

    def deleteNode(self, root, key):
        """
        Takes in a Root reference and a Key to delete.
        Case 1: Node is a Leaf
        Case 2: Node to be deleted has 1 Children
        Case 3: Node to be deleted has 2 Children

        Case 1:
        Traverse the BST till you find the next of the Node is the Key then remove the pointer and del the Key.

        """
        if root is not None:
            if root.data < key:
                # left subtree
                self.deleteNode(root.left)
            elif root.data > key:
                # right subtree
                self.deleteNode(root.right)


# driver code
if __name__ == "__main__":
    bst = BinarySearchTree()
    r = Node(50)

    # Insert new nodes
    bst.insert(None, r)
    bst.insert(r, Node(30))
    bst.insert(r, Node(20))
    bst.insert(r, Node(40))
    bst.insert(r, Node(70))
    bst.insert(r, Node(60))
    bst.insert(r, Node(90))

    # print the Nodes in in-order traversal
    bst.inorder(r)
