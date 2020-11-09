def check(i):
    if i==1:
        return True
    for k in range(2,i):
        if i%k==0:
            return False
    return True
n=int(input())
ele=[int(i) for i in str(n)]
sum=0
for i in ele:
    j=check(i)
    #print(j)
    if j:
        sum+=i
print(sum)
    
