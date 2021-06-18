"""
Let's traverse through the tree.
"""

class Node:
	def __init__(self, data):
		self.value = data
		self.left = None
		self.right = None


def in_order_traversal(node):
		# Starts with ROOT of the node.

		# If node passed is Not None.
		if node:
			# Takes it's left
			# pass this as ROOT again.
			in_order_traversal(node.left)

			print(node.value)

			in_order_traversal(node.right)


def pre_order_traversal(node):
	# starts with the ROOT node.

	# If Node exists
	if node:
		# print ROOT value
		print(node.value)

		pre_order_traversal(node.left)

		pre_order_traversal(node.right)


def post_order_traversal(node):
	# starts with ROOT Node.

	# If node exists:
	if node:
		post_order_traversal(node.left)
		post_order_traversal(node.right)

		print(node.value)


if __name__ == "__main__":
	node = Node(7)
	node.left = Node(6)
	node.right = Node(5)

	node.left.left = Node(4)
	node.left.right = Node(3)

	node.right.left = Node(2)
	node.right.right = Node(1)

	print("-----IN ORDER------")
	in_order_traversal(node)

	print("-----PRE ORDER------")
	pre_order_traversal(node)

	print("-----POST ORDER------")
	post_order_traversal(node)
