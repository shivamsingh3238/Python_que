n=int(input())
n1=n+1//2
for i in range(1,n+1):
    for j in range(i,n1):
        print(' ',end='')
    for k in range(1,i+1):
        print(k,end='')
    for l in range(k-1,0,-1):
        print(l,end='')
    print()
for i in range(n-1,0,-1):
    for j in range(i,n1):
        print(' ',end='')
    for k in range(1,i+1):
        print(k,end='')
    for l in range(k-1,0,-1):
        print(l,end='')
    print()
        

        
