"""

The above properties of Binary Search Tree provide an ordering among keys so that the operations like search, minimum and maximum can be done fast. If there is no ordering,
then we may have to compare every key to search a given key.

Searching a key:
To search a given key in Binary Search Tree, we first compare it with root, if the key is present at root, we return root. If key is greater than root’s key, we recur for
right subtree of root node. Otherwise we recur for left subtree
"""
# Utility function to search a given KEY in BST
def binary_search(root, key):
    # best cases: root is null or key is present at Root
    if root is None or root.val == key:
        return root

    # Key is greater than Root's KEY
    if root.val < key:
        return binary_search(root.right, key)

    # Key is smaller than Root's Key
    if root.val > key:
        return binary_search(root.left, key)
