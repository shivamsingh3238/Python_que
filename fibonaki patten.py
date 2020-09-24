f1,f2=0,1
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        f3=f1+f2
        f1=f2
        f2=f3
        print(f1,end=' ')
    print('\n')
