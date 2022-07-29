#binary tree implimentation 
class node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
def insertnode(root,val):
    newnode = node(val)
    if root==None:
        root = newnode
        return
    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp.left!=None:
            q.append(temp.left)
        else:
            temp.left = newnode
            break
        if temp.right!=None:
            q.append(temp.right)
        else:
            temp.right = newnode
            break
# def deleteDeepNode(root,delnode):
#     q=[]
#     q.append(root)
#     while len(q):
#         temp =q.pop(0)
#         if temp==deleteNode:
#             temp = None
#             break
#         if temp.left==delnode:
#             temp.left=None
#             break
#         else:
#             q.append(temp.left)
#         if temp.right==delnode:
#             temp.right=None
#             break
#         else:
#             q.append(temp.right)
        
        
def deleteNode(root,key):
    if root==None:
        print("empty tree!")
        return
    elif root.left==None and root.right==None:
        if root.data == key:
            root = None
            return
        else:
            print("node does not exist!")
            return
    q = []
    q.append(root)
    nodeToDelete= None
    temp = None
    lastNode = None
    while len(q):
        temp = q.pop(0)
        if temp.data == key:
            nodeToDelete = temp
        if temp.left!=None:
            lastNode = temp
            q.append(temp.left);
        if temp.right!=None:
            lastNode = temp
            q.append(temp.right)
        
    if nodeToDelete!=None:
        nodeToDelete.data= temp.data
        # deleteDeepNode(root,temp)
        if lastNode.left==temp:
            lastNode.left = None
            del temp
            
        else:
            lastNode.right=None
            del temp
def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
        
def preorder(root):
    if root == None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
    
if __name__=="__main__":
    root = node(1)
    insertnode(root,2)
    insertnode(root,3)
    insertnode(root,4)
    insertnode(root,5)
    insertnode(root,6)
    insertnode(root,7)
    insertnode(root,9)
    deleteNode(root,7)
    inorder(root)
    print()
    preorder(root)
    
   
    
    
    
    
    
    
    
