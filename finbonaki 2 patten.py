n=int(input())
j=n*(n+1)//2
t=[1,1]
for i in range(2,j):
    t.append((t[i-2]+t[i-1])%1000000007)
m=j-1
for i in range(0,n+1):
    for j in range(0,i+1):
        print(t[m],end=' '*(10-len(str(t[m]))))
        m-=1
    print('')
    
