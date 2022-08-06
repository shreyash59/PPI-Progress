class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None


def printLevelOrder(root):
	if root is None:
		return
	queue = []
	queue.append(root)

	while(len(queue) > 0):
		print(queue[0].data)
		node = queue.pop(0)

		
		if node.left is not None:
			queue.append(node.left)

		if node.right is not None:
			queue.append(node.right)



root = Node(5)
root.left = Node(2)
root.right = Node(9)
root.left.left = Node(1)
root.left.right = Node(3)

print("Level Order")
printLevelOrder(root)

