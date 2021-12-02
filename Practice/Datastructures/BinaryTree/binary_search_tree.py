"""
A Binary Search Tree is a Binary Tree
consisting of Nodes. Starting at ROOT node.

In BST Left Sub Tree values should be less than the ROOT
Node and Right Sub Tree should be greater than the ROOT
"""
class Node:
	def __init__(self, data):
		self.value = data
		self.left = None
		self.right = None


# Insert Elements to BST
# Elements adding should be comparable
def search_node(root, key):
	if root.value == key or root is None:
		return root

	if key < root.value:
		# recurse the left subtree.
		search_node(root.left, key)

	if key > root.value:
		# recurse the right subtree
		search_node(root.right, key)

	return


def insert_node(key, root):
	if key == root.value:
		pass

	if key < root.value:
		insert_node(key, root.left)

	elif key > root.value:
		insert_node(key, root.right)

	# now add node.
	if root is None:
		if root.value < key
			root.left = Node(key)

		elif root.value > key:
			root.right = Node(key)

		else:
			pass




def delete_node():
	pass


def main():
	node = Node(10)

if __name__ == '__main__':
