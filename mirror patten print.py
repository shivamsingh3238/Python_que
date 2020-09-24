n=int(input())
n=int(n/2)+1
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(' ',end='')
    for j in range(1,i):
        print(str(j)+'*' ,end='')
    print(i)
for i in range(n-1,0,-1):
    for j in range(n,i,-1):
        print(' ',end='')
    for j in range(1,i):
        print(str(j)+'*' ,end='')
    print(i)
