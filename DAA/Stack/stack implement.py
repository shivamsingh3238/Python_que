def pop(stack,k):
    #stack.remove(k)
    stack.pop()


def add_element(stack,k):
    stack.append(k)
    

n=int(input())
element=[int(input()) for i in range(n)]
stack=[]
for i in element:
    add_element(stack,i)
print(stack)

pop_element=int(input("enter the no which you want to pop"))
pop(stack,pop_element)
print(stack)

