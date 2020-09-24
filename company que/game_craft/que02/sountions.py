def find(arr,k):
    l=len(arr)
    count=0
    t=[]
    for i in range(0,l):
        if i+2>l:
           continue
        else:
            temp=[]
            for j in range(i,i+2):
                temp.append(arr[j])
            t.append(temp)
    for obj in t:
        for j in range(0,len(obj)-1,2):
            a=obj[j]^obj[j+1]
            if a==k:
                count+=1
    return count
                




n=int(input())
arr=list(map(int,input().split()))
k=int(input())
result=find(arr,k)
print(result)
