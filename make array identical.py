a=list(map(int,input().split(' ')))
b=list(map(int,input().split(' ')))
set=[]
for i in a:
    for j in range(len(b)):
        if b[j]==i:
            set.append(j)
            b[j]=0
            continue
print(set)
print(b)
    
