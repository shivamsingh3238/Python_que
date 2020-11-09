n=int(input())
ele=raw_input().split()
sum=0
for i in range(0,len(ele)):
    if i%2==0:
        sum+=int(ele[i])
print(sum)
        
