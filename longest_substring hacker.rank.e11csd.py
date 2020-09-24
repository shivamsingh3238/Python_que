##1
##5 2
##eceba
#test case
#o/p = 3

n=int(input())
while(n!=0):
    n-=1
    a,b=map(int,input().split())
    s=input()
    z=[s[i:j:1] for i in range(0,len(s)) for j in range(i+1,len(s)+1)]
    print(z)
    d=0
    for i in z:
        if len(set(list(i)))==b:
            d=max(d,len(i))
    print(d)
