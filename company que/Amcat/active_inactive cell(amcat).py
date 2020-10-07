def cal(ele,k):
    new=ele[:]
    l=len(ele)
    #boundary element
    
    for _ in range(k):
        new[0]=ele[1]
        new[l-1]=ele[l-2]
        for i in range(1,l-1):
            if ele[i-1]==ele[i+1]:
                new[i]=0
            else:
                new[i]=1
        ele=new[:]
    return ele
        



ele=list(map(int,input().split( )))
days=int(input())
ans=cal(ele,days)
for i in ans:
    print(i,end=" ")
