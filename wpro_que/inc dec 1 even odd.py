n=int(input())
ele=[int(i) for i in str(n)]
arr=[0]*len(ele)
for i in range(0,len(ele)):
    if ele[i]%2==0:
        arr[i]=ele[i]+1
    else:
        arr[i]=ele[i]-1
print(arr)
for i in arr:
    print(i,end="")
