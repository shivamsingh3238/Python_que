graph={}
n=int(input())
for i in range(0,n):
    v=input('enter the vertax  ')
    graph[v]=list(input('enter the edges  ').split(' '))
print(graph)
print('print edges')
print(graph.values())
