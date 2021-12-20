"""
Binary Tree to Binary Search Tree can be done in 3 Steps:

Step 1: Do inorder traversal of the Binary Tree and copy the elements to an Array
Step 2: Sort this array with best feasible algorithm
Step 3: Do inorder traversal of the same array and Replace the 'data' of the nodes
        once the checks are validated. This will ensure you are placing the right element
        at right location in the BST.
"""


class Node:
    """Contains Node data"""
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    # inorder traversal
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def insertData(root, new_data):
    # best case
    if root is None:
        return Node(new_data)
    
    # else do the checks and insert at the leaves
    if new_data < root.data:
        root.left = insertData(root.left, new_data)
    else:
        root.right = insertData(root.right, new_data)
    
    return root

def storeElements(root, arr):
    # Best case: If root node itself is None
    if root is None:
        return
    
    storeElements(root.left, arr)

    # Store the value
    arr.append(root.data)

    storeElements(root.right, arr)


def arr_to_bst(arr, root):
    # best case if root is none
    if root is None:
        return
    
    # update the left subtree
    arr_to_bst(arr, root.left)
    
    root.data = arr.pop(0)

    arr_to_bst(arr, root.right)


def binary_tree_to_binary_search_tree(root):
    # we take the given binary tree, traverse inorder manner
    # get the elements and store in an array each time recursively

    # Best case: If root node itself is None
    if root is None:
        return
    
    # create an empty array, pass the reference to root, and pass array.
    # to store the Binary Tree values in this array
    arr = []
    storeElements(root, arr)

    # sort the array having elements from Binary Tree
    arr.sort()

    # now take this sorted array and put elements back in Binary Tree
    # which turnsout to be a Binary Search Tree
    arr_to_bst(arr, root)


# Driver code:
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(8)
    root.left.right = Node(4)

    # Print inorder
    print("Binary Tree Inorder Traversed: ")
    inorder(root)

    # Binary tree to Binary search tree
    print("Converting into Binary Search Tree ...")
    binary_tree_to_binary_search_tree(root)

    # Print Inorder
    print("Converted into Binary Search Tree.")
    print("Binary Search Tree Inorder Traversal:")
    inorder(root)