"""
Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80
"""
# from Datastructures.BinarySearchTree.binary_search_delete_node import inorder, insert


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def insert_node(root, data):
    """We always insert node at the leaf."""
    # Base case: If tree is empty
    if root is None:
        return Node(data)
    
    # Otherwise traverse from Root to the suitable leaf
    # to insert the new node
    if data < root.data:
        root.left = insert_node(root.left, data)
    else:
        root.right = insert_node(root.right, data)
    
    return root

def inorder(root):
    """Traversing to the left most element in the tree
    then moving to the parent node then right most element
    in the tree. This traversal is called Inorder. The output
    will be a Sorted list of elements."""
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

    return

def min_of_right_subtree(root):
    """From the root node passed,
    find the minimum of that subtree"""
    min_element = root
    while min_element is not None:
        min_element = min_element.left
    return min_element

def delete_node(root, target):
    """
    Deletion has 3 scenarios:
    1. Target is Leaf
    2. Target has 1 Child node
    3. Target has 2 Child nodes
    """
    # Base case:
    if root is None:
        return None
    
    # now check till the Target is found.
    if target < root.data:
        root.left = delete_node(root.left, target)
    elif target > root.data:
        root.right = delete_node(root.right, target)
    else:
        # the node might have 0 or 1 child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        # if the node has 2 children
        # then findout the Min of right subtree
        temp = min_of_right_subtree(root)
        # now replace the Target root key with
        # minimum element we just found.
        root.data = temp.data

        # now delete the original minimum element
        # from the Right-subtree.
        root.right = delete_node(root.right, temp.data)

    return root


# Driver code.
if __name__ == "__main__":
    root = Node(50)
    
    # Insert nodes into the tree.
    insert_node(root, 30)
    insert_node(root, 20)
    insert_node(root, 40)
    insert_node(root, 60)
    insert_node(root, 70)
    insert_node(root, 80)

    # Do a Inorder traversal
    inorder(root)

    print("\n Deleting node 40. \n")
    # delete a node from the tree.
    delete_node(root, 40)

    # check if the node got deleted
    # by printing.
    inorder(root)
