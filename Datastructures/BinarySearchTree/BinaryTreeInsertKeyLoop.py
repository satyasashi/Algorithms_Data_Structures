# from Datastructures.BinarySearchTree.binaryInsertionOfKey import inorder, insert

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insertKey(self, root, key):
        """
        We start the traversal at the ROOT.
        Best case is, if the tree has no nodes, then the new KEY will be the ROOT
        Else, we change the current node to next node and run the loop again
        till we reach a leaf.

        Once we are here at a leaf, then we check the new KEY is greater or lesser
        and then insert in either 'Right' child or 'Left' child.
        """
        if root is None:
            root = Node(key)

        while root is not None:
            if key > root.data:
                prev = root
                root = root.right
            else:
                prev = root
                root = root.left
        
        if key > prev.data:
            prev.right = Node(key)
        else:
            prev.left = Node(key)
    
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.data)
            self.inOrder(root.right)

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


if __name__ == "__main__":
    # Driver code
    bst = BinarySearchTree()
    a = Node(50)

    bst.insertKey(a, 30)
    bst.insertKey(a, 20)
    bst.insertKey(a, 40)
    bst.insertKey(a, 70)
    bst.insertKey(a, 60)
    bst.insertKey(a, 90)

    bst.inOrder(a)