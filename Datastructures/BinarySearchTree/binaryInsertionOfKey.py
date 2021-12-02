# A new key is always inserted at leaf. We start searching a key from Root
# till we hit a leaf node. Once a leaf node is found, the new node is added
# as a child of the LEAF node.
"""
    100                         100
    /   \\       Insert 40       /   \
20      500     ---->       20      500
/   \\                       /   \
10  30                    10    30
                                  \
                                  40
"""
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    # Utility function to insert a new node with given KEY
    def insert(self, root, node):
        """
        If the tree is empty, make the new KEY as Root.
        Else, check if new KEY is > or < than the current
        Node value.

        If greater, then insert on right subtree.
        Else insert on left subtree.

        if either of left subtree or right subtree nodes are NOT NONE,
        it means we need to Recur till we reach a leaf.
        """
        if self.root is None:
            self.root = node

        else:
            if root.val < node.val:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)

    def inorder(self, root) -> None:
        if root:
            print(root.left is None)
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


if __name__ == "__main__":
    
    # Driver program to test the above functions
    # Let us create the following BST
    #      50
    #    /     \ 
    #   30     70
    #   / \    / \
    #  20 40  60 90

    bst = BinarySearchTree()

    # Initial Root Node
    r = Node(50)

    # Insert new nodes
    bst.insert(None, r)
    bst.insert(r, Node(30))
    bst.insert(r, Node(20))
    bst.insert(r, Node(40))
    bst.insert(r, Node(70))
    bst.insert(r, Node(60))
    bst.insert(r, Node(90))

    # Print Inorder traversal of the BST
    bst.inorder(r)
