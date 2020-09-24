class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key),end=" ")
        inorder(root.right)
        
#insert node method
def insert(node,key):
##    if node is None:
##        return node(key)
    if key < node.key:
        node.left =(insert(node.left,key))
    else:
        node.right=(insert(node.right,key))
    return node
       

root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)
print("INorder traverse")
inorder(root)
