ele=raw_input().split()
arr=[0]*len(ele)
arr[0]=int(ele[0])
#print(type(ele[0]))
for i in range(0,len(ele)-1):
    sum=int(arr[i])+int(ele[i+1])
    arr[i+1]=sum
sum=0
for i in arr:
    sum+=i
print(sum)
