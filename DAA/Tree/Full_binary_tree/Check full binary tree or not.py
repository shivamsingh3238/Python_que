class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
def check(root):
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return(check(root.left) and check(root.right))
    
            
        
        
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
if check(root):
    print("it's full binary tree")
else:
    print("Not a full binary tree")
