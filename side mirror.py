n=int(input())
s=''
l=[]
for i in range(1,n+1):
    s=s+str(i)
    l.append(s)
for i in range(0,n):
    print(l[i],end='')
    print('',end=' '*(2*i))
    print('',end=' '*(2*i))
    print(l[i][::-1],end='')
    print('')

















    
