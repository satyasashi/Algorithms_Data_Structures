from binaryInsertionOfKey import BinarySearchTree, Node

class DeleteNode(BinarySearchTree):
    """Deletes a specified key from the Binary Tree"""
    pass

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