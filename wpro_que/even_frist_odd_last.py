n=int(input())
ele=list(map(int,raw_input().split()))
arr=sorted(ele)
print(arr)
result=[]
for i in arr:
    if i%2==0:
        result.append(i)
for i in arr:
    if not(i%2==0):
        result.append(i)
print(result)
