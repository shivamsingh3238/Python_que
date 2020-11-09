ele=list(map(int,input().split()))
arr1=[int(i) for i in str(ele[0])]
arr2=[int(i) for i in str(ele[1])]
arr3=[int(i) for i in str(ele[2])]
#frist max
sum=0
v1=max(arr1)
arr1.remove(v1)
v2=max(arr2)
arr2.remove(v2)
v3=max(arr3)
arr3.remove(v3)
sum=v1+v2+v3
#secound max
sum1=0
a1=max(arr1)
arr1.remove(a1)
a2=max(arr2)
arr2.remove(a2)
a3=max(arr3)
arr3.remove(a3)
sum1=a1+a2+a3
print(sum-sum1)
