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
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Utility function to insert a new node with given KEY
def insert(root, node):
    if root is None:
        root = node

    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# Driver program to test the above functions
# Let us create the following BST
#      50
#    /     \ 
#   30     70
#   / \    / \
#  20 40  60 80

# Initial Root Node
r = Node(50)

# Insert new nodes
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(90))

# Print Inorder traversal of the BST
inorder(r)
