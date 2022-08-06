class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key
def printInorder(root):

	if root==None:
	    return
	printInorder(root.left)
	print(root.val),
	printInorder(root.right)

def printPostorder(root):

	if root==None:
	    return
		
	printPostorder(root.left)
	printPostorder(root.right)

	print(root.val)

def printPreorder(root):

	if root==None:
	    return
	    
	print(root.val)

	printPreorder(root.left)

	printPreorder(root.right)



root = Node(5)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
print("Preorder")
printPreorder(root)

print("Inorder")
printInorder(root)

print ("Postorder")
printPostorder(root)
