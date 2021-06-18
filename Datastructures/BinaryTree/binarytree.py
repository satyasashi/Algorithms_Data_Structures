# Tree whose elements have at most 2 children is called Binary Tree.
# It has :
# DATA
# Pointer to LEFT CHILD
# Pointer to RIGHT CHILD

class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


if __name__ == "__main__":
    # create Root
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    print("Created a Binary Tree.")
    print("Tree Root: {}".format(root.value))
    print("Children: {}, {}".format(root.left.value, root.right.value))
