n=int(input())
str=input()
result=''
c=0
for i in range(n-1):
    aa=str[i]
    bb=str[i+1]
    count=0
    for j in range(n-1):
        if aa==str[j] and bb==str[j+1]:
            count+=1
        if c<count:
            result=aa+bb
            c=count
print(result)
    
