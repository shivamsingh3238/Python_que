n=int(input())
i=0
while(n>i):
    n,m,q=map(int,input().split(" "))
    m1=list(map(int,input().split(" ")))
    q1=list(map(int,input().split(" ")))
    count=0
    k=0
    while(q>k):
        for j in range(0,n+1,q1[k]):
            if j not in m1 and j != 0:
                
                count+=1
        k+=1
    print("Case #1: ",end="")
    print(count)
    i+=1
            
         
    
    
