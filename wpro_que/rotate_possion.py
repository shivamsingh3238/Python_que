n,k=map(int,(input()).split())
ele=list(str(n))
arr1=ele[:k-1]
arr2=ele[k-1:]
ele1=arr2+arr1
print(ele1)
for i in ele1:
    print(i,end='')
