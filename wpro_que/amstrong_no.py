n=int(input())
l=len(str(n))
sum=0
ans=0
ele=[int(i) for i in str(n)]
for i in ele:
    sum=sum+(i**l)
if sum == n:
    for i in ele:
        if i%2==0:
            ans+=i
else:
    for i in ele:
        if not(i%2==0):
            ans+=i
print(ans)
            
    
