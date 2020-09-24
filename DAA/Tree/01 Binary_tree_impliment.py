class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key,end='')
        print('->',end='')
        if self.right:
            self.right.inorder()
#without using  class
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key),end=" ")
        inorder(root.right)
def preorder(root):
    if root:
        print(root.key,end=" ")
        print('->')
        preorder(root.left)
        preorder(root.right)



        
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
#print("in-order travrse")
#root.inorder()
print()
#inorder(root)
preorder(root)
