class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key

    #inorder traverse 
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key,end=' ')
        if self.right:
            self.right.inorder()
    #add node using level order traverse
def insert(temp,key):
        q=[]
        q.append(temp)
        while(len(q)):
            temp=q[0]
            q.pop(0)
            if temp.left:
                q.append(temp.left)
            else:
                temp.left=node(key)
                break
            if temp.right:
                q.append(temp.right)
            else:
                temp.right=node(key)
                break
            
        
        
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
print("in order travrse")
root.inorder()

nd=int(input('\n enter the no'))
insert(root,nd)
print('after adding node')
root.inorder()
